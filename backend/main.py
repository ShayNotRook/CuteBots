from typing import Annotated

from fastapi import FastAPI, Depends
# from fastapi_admin import app as admin_app

from sqlalchemy.orm import Session

from backend.models import Base
from backend.models import *
from backend.db.database import db_engine, SessionLocal
from backend.api.v1 import auth 



app = FastAPI()

Base.metadata.create_all(bind=db_engine)



