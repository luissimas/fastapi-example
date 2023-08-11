from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateMovieDTO(BaseModel):
    name: str
    release_date: datetime
    description: str
    director: str
    duration: Optional[int] = None
    budget: Optional[int] = None


class UpdateMovieDTO(BaseModel):
    name: Optional[str] = None
    release_date: Optional[datetime] = None
    description: Optional[str] = None
    director: Optional[str] = None
    duration: Optional[int] = None
    budget: Optional[int] = None
