from app.configs.database import Base
from sqlalchemy import Column, String, Integer, Boolean


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(256), unique=True, index=True)
    password = Column(String(256))
    is_active = Column(Boolean, default=True)
