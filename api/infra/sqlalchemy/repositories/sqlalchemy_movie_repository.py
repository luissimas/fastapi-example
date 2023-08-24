from uuid import UUID

from sqlalchemy.orm import Session, sessionmaker

from api.application.dtos import (
    CreateMovieDTO,
    PaginatedResult,
    PaginationParameters,
    UpdateMovieDTO,
)
from api.application.repositories.movie_repository import MovieRepository
from api.domain.entities.movie import Movie
from api.domain.exceptions import NotFoundException
from api.infra.sqlalchemy.models import MovieModel
from api.infra.sqlalchemy.repositories.utils import paginate_query


class SqlAlchemyMovieRepository(MovieRepository):
    def __init__(self, session: sessionmaker):
        self.session = session

    def create(self, movie_data: CreateMovieDTO) -> Movie:
        movie = MovieModel(**movie_data.__dict__)

        with self.session() as session:
            session.add(movie)
            session.commit()
            session.refresh(movie)

        return self.__model_to_entity(movie)

    def list(self, pagination_params: PaginationParameters) -> PaginatedResult[Movie]:
        with self.session() as session:
            query = session.query(MovieModel)
            result = paginate_query(query, pagination_params)

        return PaginatedResult(
            total=result.total,
            result=[self.__model_to_entity(model) for model in result.result],
        )

    def get_by_id(self, id: UUID) -> Movie:
        with self.session() as session:
            movie_model = self.__get_by_id(id, session)

        return self.__model_to_entity(movie_model)

    def update(self, id: UUID, movie_data: UpdateMovieDTO) -> Movie:
        with self.session() as session:
            movie = self.__get_by_id(id, session)

            for attr, value in movie_data.dict().items():
                if value is not None:
                    setattr(movie, attr, value)

            session.commit()
            session.refresh(movie)

        return self.__model_to_entity(movie)

    def delete(self, id: UUID) -> None:
        with self.session() as session:
            movie = self.__get_by_id(id, session)

            session.delete(movie)
            session.commit()

    def __get_by_id(self, id: UUID, session: Session) -> MovieModel:
        movie = session.get(MovieModel, id)

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
