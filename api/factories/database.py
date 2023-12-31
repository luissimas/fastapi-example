from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from api.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)
sessionmaker = sessionmaker(bind=engine, expire_on_commit=False)


def make_db_session():
    return sessionmaker
