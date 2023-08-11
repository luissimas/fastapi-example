from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from api.application.dtos import (
    CreateMovieDTO,
    PaginatedResult,
    PaginationParameters,
    UpdateMovieDTO,
)
from api.domain.entities.movie import Movie


class MovieRepository(ABC):
    @abstractmethod
    def create(self, movie_data: CreateMovieDTO) -> Movie:
        raise NotImplementedError

    @abstractmethod
    def list(self, pagination_params: PaginationParameters) -> PaginatedResult[Movie]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: UUID) -> Movie:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: UUID, movie_data: UpdateMovieDTO) -> Movie:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: UUID) -> None:
        raise NotImplementedError
