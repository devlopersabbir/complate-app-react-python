from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.routes import userRoutes, authRoutes
from app.configs.database import SessionLocal, engine
from app.models import userModel
from app.controllers import userController
from app.schemas.userSchema import UserCreate
from app.controllers.userController import write_user

userModel.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = userController.get_users(db, skip=skip, limit=limit)
    if not users:
        return JSONResponse(
            content={
                "message": "No user found!",
            },
            status_code=status.HTTP_404_NOT_FOUND
        )
    else:
        return users


@app.post("/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    print(user.email)
    write_user(db, user)

    return JSONResponse(
        content={
            "message": "User created successfully!"
        },
        status_code=status.HTTP_201_CREATED
    )
