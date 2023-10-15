from app.models.baseModel import BaseModels
from sqlalchemy import Column, String, Integer


class Product(BaseModels):
    title: Column(String(256))
    slug: Column(String(256), unique=True)
    description: Column(String())
    price: Column(Integer())
