from api.application.repositories.movie_repository import MovieRepository
from api.factories.database import make_db_session
from api.infra.sqlalchemy.repositories.sqlalchemy_movie_repository import (
    SqlAlchemyMovieRepository,
)


def make_movie_repository() -> MovieRepository:
    session = make_db_session()
    return SqlAlchemyMovieRepository(session)
