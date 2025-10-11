# routers/user.py
from fastapi import APIRouter, HTTPException, Depends, Request, Response
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from services.slippi_service import get_slippi_api
from slippi.slippi_characters import get_character_url
from slippi.slippi_ranks import get_rank
import time, hashlib, json
from typing import Any, Tuple

router = APIRouter(prefix="/user", tags=["user"])

# -------- tiny TTL cache (per worker) --------
_TTL_SECONDS = 120  # tune to your freshness needs
_cache: dict[str, Tuple[float, Any]] = {}  # { key: (expires_at, value) }

def _cache_get(key: str):
    v = _cache.get(key)
    if not v:
        return None
    exp, val = v
    if exp < time.time():
        _cache.pop(key, None)
        return None
    return val

def _cache_set(key: str, val: Any, ttl: int = _TTL_SECONDS):
    _cache[key] = (time.time() + ttl, val)

# -------------- helpers ----------------------
def _normalize_tag(tag: str) -> str:
    return tag.replace("-", "#")

def _compute_main(data: dict) -> dict:
    rp = data.get("ranked_profile") or {}
    chars = rp.get("characters") or []
    if not chars:
        return {"character": None, "icon_url": None}
    main_char = chars[0].get("character")
    return {
        "character": main_char,
        "icon_url": get_character_url(main_char) if main_char else None
    }

def _compute_rank(data: dict) -> dict:
    rp = data.get("ranked_profile") or {}
    elo = rp.get("rating_ordinal")
    if elo is None:
        return {"elo": None, "display_name": None, "icon_url": None}
    name = get_rank(elo) or "Unranked"
    # business rule
    name = "Grandmaster" if name == "Master 3" else name
    slug = name.lower().replace(" ", "-")
    icon_url = f"/api/static/images/ranks/{slug}.svg"
    return {"elo": elo, "display_name": name, "icon_url": icon_url}

def _etag(payload_obj: Any) -> str:
    # stable ETag over the JSON payload
    raw = json.dumps(payload_obj, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()

# -------------- data fetch -------------------
def _fetch_user_data(norm_tag: str, slippi) -> dict:
    """Fetch from Slippi with TTL cache."""
    ck = f"user-data:{norm_tag}"
    cached = _cache_get(ck)
    if cached is not None:
        return cached

    if not slippi.does_exist(norm_tag):
        raise HTTPException(status_code=404, detail=f"A player with tag '{norm_tag}' does not exist!")

    slippi_user = slippi.get_player_ranked_data(norm_tag, True)
    enc = jsonable_encoder(slippi_user)
    _cache_set(ck, enc)
    return enc

# -------------- endpoints --------------------
@router.get("/{tag}/data")
def get_user_data(tag: str, slippi=Depends(get_slippi_api), response: Response = None):
    norm = _normalize_tag(tag)
    data = _fetch_user_data(norm, slippi)
    et = _etag(data)
    response.headers["ETag"] = et
    response.headers["Cache-Control"] = "public, max-age=60, stale-while-revalidate=120"
    return data

@router.get("/{tag}/main")
def get_user_main_character(tag: str, slippi=Depends(get_slippi_api), response: Response = None):
    norm = _normalize_tag(tag)
    data = _fetch_user_data(norm, slippi)
    body = _compute_main(data)
    response.headers["Cache-Control"] = "public, max-age=300, immutable"
    return jsonable_encoder(body)

@router.get("/{tag}/rank")
def get_user_rank(tag: str, slippi=Depends(get_slippi_api), response: Response = None):
    norm = _normalize_tag(tag)
    data = _fetch_user_data(norm, slippi)
    body = _compute_rank(data)
    response.headers["Cache-Control"] = "public, max-age=300, immutable"
    return jsonable_encoder(body)

# Aggregated (fastest for frontend)
@router.get("/{tag}")
def get_user(tag: str, request: Request, slippi=Depends(get_slippi_api), response: Response = None):
    norm = _normalize_tag(tag)
    data = _fetch_user_data(norm, slippi)
    summary = {"user": data, "char": _compute_main(data), "rank": _compute_rank(data)}

    et = _etag(summary)
    if request.headers.get("if-none-match") == et:
        # 304 – client can use cached copy
        response.status_code = 304
        return

    response.headers["ETag"] = et
    response.headers["Cache-Control"] = "public, max-age=60, stale-while-revalidate=120"
    return jsonable_encoder(summary)
