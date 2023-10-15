from app.models.userModel import User
from app.schemas.userSchema import UserSchema
from sqlalchemy.orm import Session


def find_by_username(query_db: Session, query_model: User, query_with: UserSchema) -> bool:
    return query_db.query(query_model).filter(
        query_model.username == query_with.username).first()


def find_by_email(query_db: Session, query_model: User, query_with: UserSchema) -> bool:
    return query_db.query(query_model).filter(
        query_model.email == query_with.email).first()


def find_by_uuid(query_db: Session, query_model: User, uuid: str) -> bool:
    return query_db.query(query_model).filter(
        query_model.uuid == uuid).first()
