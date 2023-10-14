import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.utils.loadDotenv import loadDotenv
loadDotenv()

DABABASE_URL: str = os.environ.get("DABABASE_URL")
engine = create_engine(DABABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
