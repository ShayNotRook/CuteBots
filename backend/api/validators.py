from pydantic import BaseModel
from typing import Optional, Annotated

"""
    Pydantic Models
"""


class UserModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone_num: str
    wallet: Annotated[Optional[str], "Wallet Address"]
    currency: int = 0
    

# User Model to validate incoming login request
class UserLogin(BaseModel):
    username: str
    password: str
    
    


    
    
