from sqlalchemy import Enum


class ERoles(Enum):
    USER = "USER"
    ADMIN = "ADMIN"
    VENDOR = "VENDOR"
