from typing import Optional
from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import sessionmaker

from src.application.dtos import (
    CreateMovieDTO,
    PaginatedResult,
    PaginationParameters,
    UpdateMovieDTO,
)
from src.application.repositories.movie_repository import MovieRepository
from src.domain.entities.movie import Movie
from src.factories.database import make_db_sessionmaker
from src.infra.sqlalchemy.models import MovieModel
from src.infra.sqlalchemy.repositories.utils import paginate_query


class SqlAlchemyMovieRepository(MovieRepository):
    def __init__(self, session: sessionmaker = Depends(make_db_sessionmaker)):
        self.session = session

    def create(self, movie_data: CreateMovieDTO) -> Movie:
        with self.session.begin() as session:
            movie = MovieModel(**movie_data.__dict__)

            session.add(movie)

            return self.__model_to_entity(movie)

    def list(self, pagination_params: PaginationParameters) -> PaginatedResult[Movie]:
        with self.session.begin() as session:
            query = session.query(MovieModel)
            result = paginate_query(query, pagination_params)
            return PaginatedResult(
                total=result.total,
                result=[self.__model_to_entity(model) for model in result.result],
            )

    def get_by_id(self, id: UUID) -> Optional[Movie]:
        with self.session.begin() as session:
            movie = session.get(MovieModel, id)
            return self.__model_to_entity(movie) if movie is not None else None

    def update(self, id: UUID, movie_data: UpdateMovieDTO) -> Optional[Movie]:
        with self.session.begin() as session:
            movie = session.get(MovieModel, id)
            for attr, value in movie_data.dict().items():
                if value is not None:
                    setattr(movie, attr, value)

            return self.__model_to_entity(movie)

    def delete(self, id: UUID) -> None:
        with self.session.begin() as session:
            movie = session.get(MovieModel, id)
            session.delete(movie)

    def __model_to_entity(self, model: MovieModel) -> Movie:
        return Movie(
            id=model.id,
            name=model.name,
            release_date=model.release_date,
            director=model.director,
            description=model.description,
            duration=model.duration,
            budget=model.budget,
        )
