from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateMovieDTO(BaseModel):
    name: str
    release_date: datetime
    description: str
    director: str
    duration: Optional[int]
    budget: Optional[int]


class UpdateMovieDTO(BaseModel):
    name: Optional[str]
    release_date: Optional[datetime]
    description: Optional[str]
    director: Optional[str]
    duration: Optional[int]
    budget: Optional[int]
