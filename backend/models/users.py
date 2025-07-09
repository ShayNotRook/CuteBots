from typing import Optional

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from backend.db.database import Base
from backend.models.characters import UserCharacter


class BaseUser(Base):
    __abstract__ = True
    
    id =                Column(Integer, primary_key=True, index=True)
    username =          Column(String, index=True)

class AdminUser(BaseUser):
    __tablename__ = "admin_users"
    
    password =          Column(String)
    
    

class User(Base):
    __tablename__ = 'users'
    
    id =                Column(Integer, primary_key=True, index=True)
    first_name =        Column(String, nullable=True)
    last_name =         Column(String, nullable=True)
    username =          Column(String, index=True)
    is_admin =          Column(Boolean, default=False)
    wallet =            Column(String(length=100))
    curreny =           Column(Integer, default=0)
    characters =        Column("character_id",ForeignKey("characters.id", ondelete="SET NULL"))