import uuid
from app.configs.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.annotation import Annotated
from app.utils.utils import ERoles


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(36), unique=True, index=True,
                  default=str(uuid.uuid4()))
    name = Column(String(256))
    username: Column(String(256), unique=True, nullable=False, index=True)
    email = Column(String(256), unique=True, index=True)
    password = Column(String(256))
    role = Column(ERoles, default=ERoles.USER)
