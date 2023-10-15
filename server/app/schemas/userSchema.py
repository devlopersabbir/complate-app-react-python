from pydantic import BaseModel
from app.utils.common import ERoles


class UserSchema(BaseModel):
    name: str
    username: str
    email: str
    password: str
    role: str = ERoles


class UserUpdateSchema(BaseModel):
    name: str
    email: str
    username: str
    role: str
    password: str
