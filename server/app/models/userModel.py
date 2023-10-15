from sqlalchemy import Column, String, Enum
from app.utils.common import ERoles
from app.models.baseModel import BaseModels


class User(BaseModels):
    __tablename__ = "Users"

    name = Column(String(256), nullable=True)
    username = Column(String(256), unique=True)
    email = Column(String(256), unique=True)
    password = Column(String(256))
    role = Column(Enum(ERoles), default=ERoles.USER)
