from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends

from api.application.dtos.movie import CreateMovieDTO, UpdateMovieDTO
from api.application.dtos.pagination import PaginatedResult
from api.application.repositories.movie_repository import MovieRepository
from api.domain.entities.movie import Movie
from api.http.utils import PaginationQueryParams
from api.infra.sqlalchemy.repositories.sqlalchemy_movie_repository import (
    SqlAlchemyMovieRepository,
)

router = APIRouter()


@router.post("", status_code=HTTPStatus.CREATED)
def create_movie(
    data: CreateMovieDTO,
    movie_repository: MovieRepository = Depends(SqlAlchemyMovieRepository),
) -> Movie:
    return movie_repository.create(data)


@router.get("")
def list_movies(
    pagination_params: PaginationQueryParams,
    movie_repository: MovieRepository = Depends(SqlAlchemyMovieRepository),
) -> PaginatedResult[Movie]:
    return movie_repository.list(pagination_params)


@router.get("/{movie_id}")
def get_movie_by_id(
    movie_id: UUID,
    movie_repository: MovieRepository = Depends(SqlAlchemyMovieRepository),
) -> Movie:
    return movie_repository.get_by_id(movie_id)


@router.patch("/{movie_id}")
def update_movie(
    movie_id: UUID,
    movie_data: UpdateMovieDTO,
    movie_repository: MovieRepository = Depends(SqlAlchemyMovieRepository),
) -> Movie:
    return movie_repository.update(movie_id, movie_data)


@router.delete("/{movie_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_movie(
    movie_id: UUID,
    movie_repository: MovieRepository = Depends(SqlAlchemyMovieRepository),
) -> None:
    return movie_repository.delete(movie_id)
