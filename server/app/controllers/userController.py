from sqlalchemy.orm import Session
from app.models.userModel import User
from app.schemas.userSchema import UserSchema, UserUpdateSchema
from app.services.services import hash_password


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def write_user(db: Session, user: UserSchema):
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


def update_user(db: Session, user_data, isUser: User):
    return user_data
    if user_data.name:
        isUser.name = user_data.name
    if user_data.username:
        isUser.username = user_data.username
    if user_data.email:
        isUser.email = user_data.email
    if user_data.role:
        isUser.role = user_data.role
    if user_data.password:
        isUser.password = hash_password(user_data.password)

    db.commit()
    db.refresh()
