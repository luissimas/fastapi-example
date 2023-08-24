from datetime import date
from uuid import UUID, uuid4

from api.application.dtos.movie import CreateMovieDTO, UpdateMovieDTO
from api.application.dtos.pagination import PaginatedResult, PaginationParameters
from api.application.repositories.movie_repository import MovieRepository
from api.domain.entities.movie import Movie


class MockedMovieRepository(MovieRepository):
    mocked_movie = Movie(
        id=uuid4(),
        name="any-name",
        release_date=date.today(),
        director="any-director",
        description="any-description",
        duration=1000,
        budget=10000,
    )

    def create(self, movie_data: CreateMovieDTO) -> Movie:
        return self.mocked_movie

    def list(self, pagination_params: PaginationParameters) -> PaginatedResult[Movie]:
        return PaginatedResult(result=[self.mocked_movie], total=1)

    def get_by_id(self, id: UUID) -> Movie:
        return self.mocked_movie

    def update(self, id: UUID, movie_data: UpdateMovieDTO) -> Movie:
        return self.mocked_movie

    def delete(self, id: UUID) -> None:
        return
