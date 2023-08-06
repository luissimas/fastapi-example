from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from uuid import UUID

from src.domain.entities.movie import Movie


@dataclass
class MovieRepositoryCreateDTO:
    name: str
    release_date: datetime
    description: str
    director: str
    duration: Optional[int]
    budget: Optional[int]


@dataclass
class MovieRepositoryUpdateDTO:
    name: Optional[str]
    release_date: Optional[datetime]
    description: Optional[str]
    director: Optional[str]
    duration: Optional[int]
    budget: Optional[int]


class MovieRepository(ABC):
    @abstractmethod
    def create(self, movie_data: MovieRepositoryCreateDTO) -> Movie:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[Movie]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: UUID) -> Optional[Movie]:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: UUID, movie_data: MovieRepositoryUpdateDTO) -> Optional[Movie]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: UUID) -> None:
        raise NotImplementedError
