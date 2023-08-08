from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID


@dataclass
class Movie:
    id: UUID
    name: str
    release_date: datetime
    director: str
    description: Optional[str] = None
    duration: Optional[int] = None
    budget: Optional[int] = None
