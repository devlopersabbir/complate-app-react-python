import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


DABABASE_URL = os.environ.get("DABABASE_URL")


engine = create_engine(DABABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()