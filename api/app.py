from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from api.routes import movie_router

app = FastAPI()

app.include_router(movie_router, prefix="/movie", tags=["Movies"])


def custom_openapi():
    """Generates custom OpenAPI metadata."""
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Movies API",
        version="0.1.0",
        summary="API de exemplo para a rotina de compartilhamento",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
