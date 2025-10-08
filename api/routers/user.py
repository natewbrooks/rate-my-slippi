from fastapi import APIRouter, HTTPException, Depends
from services.slippi_service import get_slippi_api
from slippi.slippi_characters import get_character_url
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/{tag}")
def get_user(tag: str, slippi=Depends(get_slippi_api)):
    tag = tag.replace("-", "#")
    if(slippi.does_exist(tag)):
        slippi_user = slippi.get_player_ranked_data(tag, True)
        return jsonable_encoder(slippi_user)
    else:
        raise HTTPException(status_code=404, detail=f"A player with tag '{tag}' does not exist!")


@router.get("/{tag}/main")
def get_user_main_character(tag: str, slippi=Depends(get_slippi_api)):
    data = get_user(tag, slippi=slippi)
    main_char = data.get("ranked_profile").get("characters")[0]["character"]
    return {"character": main_char, "icon_url": get_character_url(main_char)}