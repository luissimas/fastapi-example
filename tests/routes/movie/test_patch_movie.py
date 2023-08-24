from datetime import date
from http import HTTPStatus
from uuid import uuid4

from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from pytest import fixture

from api.app import app
from api.application.dtos.movie import CreateMovieDTO, UpdateMovieDTO
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
    Test cases for PATCH /movie/{movie_id} route.
    """

    def test_patch_movie_all_fields_return_ok(self, app_dependencies, mocker):
        """
        Should return HTTPStatus.OK and patched Movie data when all fields are
        provided.
        """
        movie_id = uuid4()
        data = UpdateMovieDTO(
            name="any-name",
            release_date=date.today(),
            description="any-description",
            director="any-director",
            duration=120,
            budget=1000000,
        ).model_dump(mode="json")
        result_data = jsonable_encoder(mocked_movie_repository.mocked_movie)

        spy = mocker.spy(mocked_movie_repository, "update")
        spy.return_value = result_data

        response = client.patch(f"/movie/{movie_id}", json=data)

        spy.assert_called_once_with(movie_id, UpdateMovieDTO(**data))
        assert response.status_code == HTTPStatus.OK
        assert response.json() == result_data

    def test_patch_movie_partial_fields_return_ok(self, app_dependencies, mocker):
        """
        Should return HTTPStatus.OK and patched MOVIE data fields are partially
        provided.
        """
        movie_id = uuid4()
        data = UpdateMovieDTO(
            name="any-name",
            description="any-description",
        ).model_dump(mode="json")
        result_data = jsonable_encoder(mocked_movie_repository.mocked_movie)

        spy = mocker.spy(mocked_movie_repository, "update")
        spy.return_value = result_data

        response = client.patch(f"/movie/{movie_id}", json=data)

        spy.assert_called_once_with(movie_id, UpdateMovieDTO(**data))
        assert response.status_code == HTTPStatus.OK
        assert response.json() == result_data

    def test_patch_movie_return_not_found(self, app_dependencies, mocker):
        """
        Should return HTTPStatus.NOT_FOUND and error message if the MovieModel is not
        found.
        """
        movie_id = uuid4()
        data = UpdateMovieDTO(
            name="any-name",
            release_date=date.today(),
            description="any-description",
            director="any-director",
            duration=120,
            budget=1000000,
        ).model_dump(mode="json")

        spy = mocker.spy(mocked_movie_repository, "update")
        spy.side_effect = NotFoundException("MovieModel")

        response = client.patch(f"/movie/{movie_id}", json=data)

        spy.assert_called_once_with(movie_id, UpdateMovieDTO(**data))
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.json() == {"message": "MovieModel not found"}
