import uuid
from app.configs.database import Base
from sqlalchemy import Column, String, Integer, DateTime, Enum
from app.utils.common import ERoles
import datetime


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(36), unique=True,
                  default=str(uuid.uuid4()))
    name = Column(String(256), nullable=True)
    username = Column(String(256), unique=True)
    email = Column(String(256), unique=True)
    password = Column(String(256))
    role = Column(Enum(ERoles), default=ERoles.USER)

    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now(),
                        onupdate=datetime.datetime.now())
