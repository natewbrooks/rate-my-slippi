from fastapi import APIRouter, HTTPException, Depends
from services.slippi_service import get_slippi_api

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# returns user data or null if not exist
@router.get("/{tag}")
def get_user(tag: str, slippi=Depends(get_slippi_api)):
    tag = tag.replace("-", "#")
    slippi_user = slippi.get_player_ranked_data(tag, True)
    return slippi_user