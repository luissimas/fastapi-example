from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID


@dataclass
class Movie:
    id: UUID
    name: str
    release_date: datetime
    description: str
    director: str
    duration: Optional[int]
    budged: Optional[int]
