import uuid
from typing import Optional

from pydantic import BaseModel


class Project(BaseModel):
    key: str
    description: str
    period: str
    project_id: Optional[uuid.UUID] = None
