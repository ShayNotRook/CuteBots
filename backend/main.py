from typing import Annotated, Optional

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from backend.db import models as db_models
from backend.db.database import db_engine, SessionLocal
from backend.api.routes import router
from backend.api.validators import UserModel


app = FastAPI()
app.include_router(router)

db_models.Base.metadata.create_all(bind=db_engine)


# Database handler
async def get_db():
    db = await SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dependencies injection
db_dependency = Annotated[Session, Depends(get_db)]


@app.get('/')
async def home():
    return {"message": "Welcome"}


# API Endpoints
@app.post('/users/create/')
async def create_user(user: UserModel, db: db_dependency, user_data: dict):
    user_schema : UserModel = user(**user_data)
    db_item =  db_models.User(**user_schema.model_dump())
    
    session = SessionLocal()
    
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    session.close()
    
    return db_item


@app.post("/users/login/")
async def login(user: UserModel, db: db_dependency, user_data: dict):
    pass