import datetime
from pydantic import BaseModel
from app.utils.common import ERoles


class UserCreate(BaseModel):
    name: str
    username: str
    email: str
    password: str
    role: str = ERoles
