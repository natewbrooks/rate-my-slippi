from functools import lru_cache
from slippi.slippi_api import SlippiRankedAPI
from slippi.slippi_characters import get_character_url

@lru_cache()
def get_slippi_api() -> SlippiRankedAPI:
    return SlippiRankedAPI()

@lru_cache()
def get_slippi_character_icon() -> str:
    return get_character_url() 