from pydantic import BaseModel
from app.utils.common import ERoles
from typing import Optional


class UserSchema(BaseModel):
    name: str
    username: str
    email: str
    password: str
    role: str = ERoles


class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    username: Optional[str] = None
    role: Optional[str] = None
    password: Optional[str] = None


class UserLoginSchema(BaseModel):
    username: str
    password: str
