from fastapi import Request
from fastapi.responses import JSONResponse

from api.domain.exceptions import NotFoundException


def not_found_exception_handler(request: Request, exception: NotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": str(exception)},
    )
