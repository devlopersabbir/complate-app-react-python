import uuid
from app.configs.database import Base
from sqlalchemy import Column, String, Integer, DateTime
import datetime


class BaseModels(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(36), unique=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now(),
                        onupdate=datetime.datetime.now())
