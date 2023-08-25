from http import HTTPStatus

from fastapi import Request
from fastapi.responses import JSONResponse

from api.domain.exceptions import NotFoundException


def not_found_exception_handler(request: Request, exception: NotFoundException):
    return JSONResponse(
        status_code=HTTPStatus.NOT_FOUND, content={"message": str(exception)}
    )
