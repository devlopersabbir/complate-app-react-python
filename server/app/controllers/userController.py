from fastapi.responses import JSONResponse
from fastapi import status
from sqlalchemy.orm import Session
from app.models.userModel import User
from app.schemas.userSchema import UserCreate
from app.services.services import hash_password


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def write_user(db: Session, user: UserCreate) -> User:
    db_user = User(
        name=user.name,
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
