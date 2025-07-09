from typing import Annotated

from fastapi import Depends

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'sqlite:///./cutedb.sqlite3'


db_engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

# This base is used for DB models
Base = declarative_base()


async def get_db():
    db = await SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dependecy injection for db connection annotation (type hint)
db_dependency = Annotated[Session, Depends(get_db)]
