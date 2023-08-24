from http import HTTPStatus

from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from pytest import fixture

from api.app import app
from api.application.dtos.movie import CreateMovieDTO
from api.application.dtos.pagination import PaginationParameters
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
    Test cases for GET /movie route.
    """

    def test_list_movie_return_ok_without_pagination_params(
        self,
        app_dependencies,
        mocker,
    ):
        """
        Should return HTTPStatus.OK and paginated result when no pagination
        params are provided.
        """
        spy = mocker.spy(mocked_movie_repository, "list")

        response = client.get("/movie")

        spy.assert_called_once_with(PaginationParameters())
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {
            "total": 1,
            "result": [jsonable_encoder(mocked_movie_repository.mocked_movie)],
        }

    def test_list_movie_return_ok_with_pagination_params(
        self,
        app_dependencies,
        mocker,
    ):
        """
        Should return HTTPStatus.OK and paginated result when pagination
        params are provided.
        """
        spy = mocker.spy(mocked_movie_repository, "list")

        response = client.get("/movie?skip=42&limit=13")

        spy.assert_called_once_with(PaginationParameters(skip=42, limit=13))
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {
            "total": 1,
            "result": [jsonable_encoder(mocked_movie_repository.mocked_movie)],
        }
