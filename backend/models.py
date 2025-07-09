from typing import Optional

from sqlalchemy import Boolean, Integer, String, Column, ForeignKey

from backend.db.database import Base


class BaseCharacter(Base):
    __abstract__ = True
    
    id =                Column(Integer, primary_key=True, index=True)
    name =              Column(String(length=250))
        

class UserCharacter(BaseCharacter):
    __tablename__ = True
    
    currency =          Column(Integer)
    
    

    
    