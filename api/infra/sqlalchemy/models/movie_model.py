from uuid import uuid4

from sqlalchemy import Column, Date, Integer, String, Uuid

from api.infra.sqlalchemy.models.base import Base


class MovieModel(Base):
    __tablename__ = "movies"

    id = Column(Uuid, primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    director = Column(String, nullable=False)
    description = Column(String, default=None)
    duration = Column(Integer, default=None)
    budget = Column(Integer, default=None)
