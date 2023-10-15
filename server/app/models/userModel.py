from sqlalchemy import Column, String, Enum, event
from app.utils.common import ERoles
from app.models.baseModel import BaseModels
from app.services.services import hash_password


class User(BaseModels):
    __tablename__ = "Users"

    name = Column(String(256), nullable=True)
    username = Column(String(256), unique=True)
    email = Column(String(256), unique=True)
    password = Column(String(256))
    role = Column(Enum(ERoles), default=ERoles.USER)


def before_hash_password(mapper, connection, target):
    target.password = hash_password(target.password)


event.listen(User, "before_insert", before_hash_password)
