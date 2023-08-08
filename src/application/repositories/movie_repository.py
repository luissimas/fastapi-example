from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from src.application.dtos import (
    CreateMovieDTO,
    PaginatedResult,
    PaginationParameters,
    UpdateMovieDTO,
)
from src.domain.entities.movie import Movie


class MovieRepository(ABC):
    @abstractmethod
    def create(self, movie_data: CreateMovieDTO) -> Movie:
        raise NotImplementedError

    @abstractmethod
    def list(self, pagination_params: PaginationParameters) -> PaginatedResult[Movie]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: UUID) -> Optional[Movie]:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: UUID, movie_data: UpdateMovieDTO) -> Optional[Movie]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: UUID) -> None:
        raise NotImplementedError
