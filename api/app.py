from uuid import UUID

from fastapi import Depends, FastAPI

from api.application.dtos.movie import CreateMovieDTO, UpdateMovieDTO
from api.application.dtos.pagination import PaginatedResult
from api.application.repositories.movie_repository import MovieRepository
from api.domain.entities.movie import Movie
from api.domain.exceptions.not_found_exception import NotFoundException
from api.infra.sqlalchemy.repositories.sqlalchemy_movie_repository import (
    SqlAlchemyMovieRepository,
)
from api.routes.utils import PaginationQueryParams

app = FastAPI()


@app.post("/movie")
def create_movie(
    data: CreateMovieDTO,
    movie_repository: MovieRepository = Depends(SqlAlchemyMovieRepository),
) -> Movie:
    return movie_repository.create(data)


@app.get("/movie")
def list_movies(
    pagination_params: PaginationQueryParams,
    movie_repository: MovieRepository = Depends(SqlAlchemyMovieRepository),
) -> PaginatedResult[Movie]:
    return movie_repository.list(pagination_params)


@app.get("/movie/{movie_id}")
def get_movie_by_id(
    movie_id: UUID,
    movie_repository: MovieRepository = Depends(SqlAlchemyMovieRepository),
) -> Movie:
    return movie_repository.get_by_id(movie_id)


@app.patch("/movie/{movie_id}")
def update_movie(
    movie_id: UUID,
    movie_data: UpdateMovieDTO,
    movie_repository: MovieRepository = Depends(SqlAlchemyMovieRepository),
) -> Movie:
    return movie_repository.update(movie_id, movie_data)


@app.delete("/movie/{movie_id}")
def delete_movie(
    movie_id: UUID,
    movie_repository: MovieRepository = Depends(SqlAlchemyMovieRepository),
) -> None:
    return movie_repository.delete(movie_id)
