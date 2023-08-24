from http import HTTPStatus

from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from pytest import fixture

from api.app import app
from api.application.dtos.movie import CreateMovieDTO
from api.factories.repositories import make_movie_repository
from tests.mocks import MockedMovieRepository

client = TestClient(app)
mocked_movie_repository = MockedMovieRepository()


@fixture
def app_dependencies():
    app.dependency_overrides[make_movie_repository] = lambda: mocked_movie_repository
    yield
    app.dependency_overrides = {}


class TestCreateMovie:
    """
    Test cases for POST /movie route.
    """

    def test_create_movie_return_created(self, app_dependencies, mocker):
        """
        Should return HTTPStatus.CREATED and created movie data.
        """
        data = jsonable_encoder(mocked_movie_repository.mocked_movie)
        data_without_id = {key: value for key, value in data.items() if key != "id"}

        spy = mocker.spy(mocked_movie_repository, "create")

        response = client.post(f"/movie", json=data_without_id)

        spy.assert_called_once_with(CreateMovieDTO(**data))
        assert response.status_code == HTTPStatus.CREATED
        assert response.json() == data
