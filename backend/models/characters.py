from typing import Annotated

from fastapi import FastAPI
from sqlalchemy import Column, Integer, String

from backend.db.database import Base

class BaseCharacter(Base):
    __abstract__ = True
    
    id =                    Column(Integer, primary_key=True, index=True)
    name =                  Column(String)
    exp =                   Column(Integer, default=0)
    level =                 Column(Integer, default=1)
    
class UserCharacter(BaseCharacter):
    __tablename__ = "characters"
    
    