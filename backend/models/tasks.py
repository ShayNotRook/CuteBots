from sqlalchemy import Column, Boolean, Integer, String

from backend.db.database import Base

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
    