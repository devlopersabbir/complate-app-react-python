from sqlalchemy.orm import Session
from app.models.productModel import Product


def getAllProduct(db: Session):
    db.query(Product).all()
