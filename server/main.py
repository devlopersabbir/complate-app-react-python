from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routes import authRoutes, userRoutes, productRoutes
from app.configs.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(authRoutes.router, prefix="/api/v1/auth")
app.include_router(userRoutes.router, prefix="/api/v1/users")
app.include_router(productRoutes.router, prefix="/api/v1/products")


@app.get("/", tags=["Checker"])
async def checker():
    return JSONResponse(
        content={
            "Working": True,
            "Hello": "World"
        }
    )
