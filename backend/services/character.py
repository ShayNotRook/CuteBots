from fastapi.responses import HTMLResponse

from backend.db.database import Base
from backend.models.characters import UserCharacter
from backend.models.users import User

async def create_character(name: str, user: User):
    character = UserCharacter(name=name)
    

async def get_xp_cap(character: UserCharacter):
    xp_required = character.level * 100 / 2
    
    return xp_required

async def add_xp(character: UserCharacter, amount: int):
    character.exp += amount
    while character.exp >= get_xp_cap(character):
        character.exp = 0
        character.level += 1
    return character