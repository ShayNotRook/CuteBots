from typing import Optional

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from backend.db.database import Base



class BaseUser(Base):
    __abstract__ = True
    
    id =                Column(Integer, primary_key=True, index=True)
    phone_num =         Column()


class AdminUser(BaseUser):
    __tablename__ = "Users"
    
    
    

class User(Base):
    __tablename__ = 'Users'
    
    id =                Column(Integer, primary_key=True, index=True)
    first_name =        Column(Optional[String])
    last_name =         Column(Optional[String])
    username =          Column(String, index=True)
    password =          Column(String)
    is_admin =          Column(Boolean, default=False)
    wallet =            Column(String(length=100))
    curreny =           Column(Integer, default=0)
    characters =        Column(ForeignKey("db.models.UserCharacter", ondelete="SET NULL"))