import uuid
from typing import Optional

from pydantic import BaseModel


class Period(BaseModel):
    period_id: Optional[uuid.UUID] = None
    period_name: str
