from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from src.application.dtos import (
    CreateMovieDTO,
    PaginatedResult,
    PaginationParameters,
    UpdateMovieDTO,
)
from src.application.repositories.movie_repository import MovieRepository
from src.domain.entities.movie import Movie
from src.domain.exceptions import NotFoundException
from src.factories.database import make_db_session
from src.infra.sqlalchemy.models import MovieModel
from src.infra.sqlalchemy.repositories.utils import paginate_query


class SqlAlchemyMovieRepository(MovieRepository):
    def __init__(self, session: Session = Depends(make_db_session)):
        self.session = session

    def create(self, movie_data: CreateMovieDTO) -> Movie:
        movie = MovieModel(**movie_data.__dict__)

        self.session.add(movie)
        self.session.commit()
        self.session.refresh(movie)

        return self.__model_to_entity(movie)

    def list(self, pagination_params: PaginationParameters) -> PaginatedResult[Movie]:
        query = self.session.query(MovieModel)
        result = paginate_query(query, pagination_params)
        return PaginatedResult(
            total=result.total,
            result=[self.__model_to_entity(model) for model in result.result],
        )

    def get_by_id(self, id: UUID) -> Movie:
        movie_model = self.__get_by_id(id)
        return self.__model_to_entity(movie_model)

    def update(self, id: UUID, movie_data: UpdateMovieDTO) -> Movie:
        movie = self.__get_by_id(id)

        for attr, value in movie_data.dict().items():
            if value is not None:
                setattr(movie, attr, value)

        self.session.commit()
        self.session.refresh(movie)

        return self.__model_to_entity(movie)

    def delete(self, id: UUID) -> None:
        movie = self.__get_by_id(id)

        self.session.delete(movie)
        self.session.commit()

    def __get_by_id(self, id: UUID) -> MovieModel:
        movie = self.session.get(MovieModel, id)

        if movie:
            return movie

        raise NotFoundException("Movie")

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
