from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.configs.database import get_db
from app.models.productModel import Product
from app.controllers.productController import getAllProduct

router = APIRouter()


@router.get("/", tags=["Get Product"])
async def get_all_product(db: Session = Depends(get_db)):
    products = getAllProduct(db)
    if not products:
        return JSONResponse(
            content={
                "message": "No Product Avaiable!",
            },
            status_code=status.HTTP_404_NOT_FOUND
        )

    return products
