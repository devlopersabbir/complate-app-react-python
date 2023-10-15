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
        password=user.password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_data: UserUpdateSchema, isUser: User):
    for key, value in user_data.dict().items():
        if key == "password" and value is not None:
            # Hash the provided password and set it to the isUser object
            hashedPassword = hash_password(value)
            setattr(isUser, key, hashedPassword)
        elif value is not None:
            # For other fields (e.g., username), set the values directly
            setattr(isUser, key, value)

    db.commit()
    db.refresh(isUser)
    return isUser
