from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import DATABASE_URL


def make_db_sessionmaker():
    engine = create_engine(DATABASE_URL, echo=True)
    return sessionmaker(bind=engine, expire_on_commit=False)
