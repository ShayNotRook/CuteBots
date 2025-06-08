from typing import Optional

from sqlalchemy import Boolean, Integer, String, Column, ForeignKey

from backend.db.database import Base

"""
    Models for DB Schemas
"""


class BaseUser(Base):
    __abstract__ = True
    
    id =                Column(Integer, primary_key=True, index=True)
    phone_num =         Column()


class AdminUser(BaseUser):
    __tablename__ = "Users"
    
    
    

class User(Base):
    __tablename__ = 'Users'
    
    id =                Column(Integer, primary_key=True, index=True)
    first_name =        Column(Optional)
    last_name =         Column(String)
    username =          Column(String, index=True)
    password =          Column(String)
    is_admin =          Column(Boolean, default=False)
    wallet =            Column(String(length=100))
    curreny =           Column(Integer, default=0)
    
    
class BaseTask(Base):
    __abstract__ = True
    
    id =                Column(Integer, index=True, primary_key=True)
    description =       Column(String, index=True)
    is_done =           Column(Boolean, default=False)
    
    
class DailyTasks(BaseTask):
    __tablename__ = 'Daily Tasks'
    
    prize =             Column(Integer)
    
class MainTasks(BaseTask):
    __tablename__ = 'Main Tasks'
    
    
    