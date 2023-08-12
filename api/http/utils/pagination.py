from fastapi import Depends
from typing_extensions import Annotated

from api.application.dtos import PaginationParameters

PaginationQueryParams = Annotated[PaginationParameters, Depends(PaginationParameters)]
