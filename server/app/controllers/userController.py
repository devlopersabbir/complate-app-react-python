from sqlalchemy.orm import Session
from app.models.userModel import User
from app.schemas.userSchema import UserCreate


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def write_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "___notreallyhashed"
    db_user = User(
        email=user.email,
        hashed_password=fake_hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
