from pydantic import BaseModel


class ProductSchema(BaseModel):
    title: str
    slug: str
    description: str
    price: int
