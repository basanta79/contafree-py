import uuid
from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel

@dataclass
class Project(BaseModel):
    project_id: Optional[uuid.UUID]
    key: str
    description: str
    period: str
