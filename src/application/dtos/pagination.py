from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, NonNegativeInt


class PaginationParameters(BaseModel):
    skip: Optional[NonNegativeInt] = 0
    limit: Optional[NonNegativeInt] = 20


T = TypeVar("T")


class PaginatedResult(BaseModel, Generic[T]):
    result: List[T]
    total: int
