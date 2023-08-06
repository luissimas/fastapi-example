from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from src.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
