from fastapi import APIRouter, HTTPException
from backend.db.database import db_dependency


router = APIRouter(prefix='/user', tags=['users'])


