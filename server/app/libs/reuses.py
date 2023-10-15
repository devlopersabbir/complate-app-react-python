from app.models.userModel import User
from app.schemas.userSchema import UserCreate


def find_by_username(query_db, query_model: User, query_with: UserCreate) -> bool:
    return query_db.query(query_model).filter(
        query_model.username == query_with.username).first()


def find_by_email(query_db, query_model: User, query_with: UserCreate) -> bool:
    return query_db.query(query_model).filter(
        query_model.email == query_with.email).first()
