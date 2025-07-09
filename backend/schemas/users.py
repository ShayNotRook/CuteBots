from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str


class UserRegister(BaseModel):
    telegram_id: str
    telegram_phone_num: str
    username: str
    name: str
    password: str    
    
