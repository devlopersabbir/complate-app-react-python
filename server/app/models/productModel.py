from app.models.baseModel import BaseModels
from sqlalchemy import Column, String, Float, Text


class Product(BaseModels):
    __tablename__ = "Products"

    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False, default=0.0)
