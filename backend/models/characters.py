from typing import Annotated

from fastapi import FastAPI
from sqlalchemy import Column



class UserCharacter():
    id:         Column(primary_key=True, index=True)
