# routers/review.py
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime, timezone, timedelta
import re
from typing import List, Optional

router = APIRouter(prefix="/reviews", tags=["reviews"])

# --- Models ---
class Review(BaseModel):
    id: UUID
    created_by: UUID
    recipient: UUID
    content: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    was_edited: bool
    upvotes: int = 0

class ReviewsResponse(BaseModel):
    tag: str = Field(..., description="Canonical Slippi tag (e.g. nful#933)")
    total: int
    items: List[Review]

# --- Helpers ---
_TAG_RE = re.compile(r"^[A-Za-z]{1,4}([#-])[0-9]{1,3}$")

def normalize_tag(raw: str) -> str:
    """
    Accepts 'nful-933' or 'nful#933' and returns canonical 'nful#933'.
    Raises 400 if format is invalid.
    """
    m = _TAG_RE.fullmatch(raw)
    if not m:
        raise HTTPException(
            status_code=400,
            detail="Invalid tag format. Expected 1-4 letters, separator (# or -), and 1-3 digits."
        )
    return raw.replace("-", "#")

# --- Routes ---
@router.get("/{tag}", response_model=ReviewsResponse, summary="Get reviews for a user tag (dummy)")
def get_reviews_for_tag(
    tag: str,
    limit: int = Query(10, ge=1, le=100, description="Max number of reviews to return"),
) -> ReviewsResponse:
    canonical = normalize_tag(tag)

    # Dummy data only (no DB yet)
    now = datetime.now(timezone.utc)
    r1 = Review(
        id=uuid4(),
        created_by=uuid4(),
        recipient=uuid4(),  # would be the user's UUID after a user lookup
        content="GGs. Neutral was strong, punish game needs work.",
        created_at=now - timedelta(days=2, hours=3),
        updated_at=now - timedelta(days=2, hours=3),
        was_edited=False,
        upvotes=12,
    )
    r2 = Review(
        id=uuid4(),
        created_by=uuid4(),
        recipient=r1.recipient,
        content="Great set. Scary edgeguards. Thanks for the games!",
        created_at=now - timedelta(hours=5),
        updated_at=now - timedelta(hours=3),  # edited once
        was_edited=True,
        upvotes=5,
    )

    items = [r1, r2][:limit]
    return ReviewsResponse(tag=canonical, total=len(items), items=items)
