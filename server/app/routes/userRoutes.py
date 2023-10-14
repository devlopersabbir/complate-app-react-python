from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.configs.database import get_db
from app.controllers.userController import get_users, write_user
from app.schemas.userSchema import UserCreate

router = APIRouter()


@router.get("/", tags=["Get User"])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    if not users:
        return JSONResponse(
            content={
                "message": "No user found!",
            },
            status_code=status.HTTP_404_NOT_FOUND
        )
    else:
        return users


@router.post("/", tags=["Create User"])
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    write_user(db, user)

    return JSONResponse(
        content={
            "message": "User created successfully!"
        },
        status_code=status.HTTP_201_CREATED
    )
