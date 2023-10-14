from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from app.routes import userRoutes
from app.configs.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(userRoutes.router, prefix="/api/v1/users")


@app.get("/", tags=["Checker"])
async def checker():
    return JSONResponse(
        content={
            "Working": True,
            "Hello": "World"
        }
    )
