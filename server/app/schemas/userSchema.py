from pydantic import BaseModel
from app.utils.utils import ERoles


class UserCreate(BaseModel):
    name: str
    username: str
    email: str
    password: str
    role: str = ERoles
