from http import HTTPStatus
from uuid import uuid4

from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from pytest import fixture

from api.app import app
from api.application.dtos.movie import CreateMovieDTO
from api.application.dtos.pagination import PaginationParameters
from api.domain.exceptions.not_found_exception import NotFoundException
from api.factories.repositories import make_movie_repository
from tests.mocks import MockedMovieRepository

client = TestClient(app)
mocked_movie_repository = MockedMovieRepository()


@fixture
def app_dependencies():
    app.dependency_overrides[make_movie_repository] = lambda: mocked_movie_repository
    yield
    app.dependency_overrides = {}


class TestListMovie:
    """
    Test cases for GET /movie/{movie_id} route.
    """

    def test_get_movie_by_id_return_ok(self, app_dependencies, mocker):
        """
        Should return HTTPStatus.OK and movie data.
        """
        movie_id = uuid4()

        spy = mocker.spy(mocked_movie_repository, "get_by_id")

        response = client.get(f"/movie/{movie_id}")

        spy.assert_called_once_with(movie_id)
        assert response.status_code == HTTPStatus.OK
        assert response.json() == jsonable_encoder(mocked_movie_repository.mocked_movie)

    def test_get_movie_by_id_return_not_found(self, app_dependencies, mocker):
        """
        Should return HTTPStatus.NOT_FOUND and error message if the movie is not
        found.
        """
        movie_id = uuid4()

        spy = mocker.spy(mocked_movie_repository, "get_by_id")
        spy.side_effect = NotFoundException("Movie")

        response = client.get(f"/movie/{movie_id}")

        spy.assert_called_once_with(movie_id)
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.json() == {"message": "Movie not found"}
