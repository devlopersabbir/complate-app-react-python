from sqlalchemy import Column, Integer, String
from app.configs.database import Base


class User(Base):
    __tablename__: "User"

    id: Column(Integer, primary_key=True, index=True)
    username: Column(String(16), unique=True, index=True)
    password: Column(String)
