from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.configs.database import get_db
from app.controllers.userController import get_users, write_user
from app.schemas.userSchema import UserCreate
from app.models.userModel import User

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
    try:
        # find user with username
        isUser = db.query(User).filter(User.username == user.username).first()
        # check if user is already is exist or not
        if isUser:
            return JSONResponse(
                content={
                    "message": "Username already exists"
                },
                status_code=status.HTTP_400_BAD_REQUEST
            )
        # Create user and send response
        write_user(db, user)
        return JSONResponse(
            content={
                "message": "Account created successfully!",
                "user": user
            },
            status_code=status.HTTP_201_CREATED
        )
    except Exception as err:
        return JSONResponse(
            content={
                "message": "Something went wrong!",
                "error": err
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
