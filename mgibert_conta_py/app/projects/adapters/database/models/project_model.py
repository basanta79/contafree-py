import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ProjectModel(Base):
    __tablename__ = "projects"

    project_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    key = Column("project_key", String, nullable=False)
    description = Column("description", String, nullable=False)
    period = Column("period", String, nullable=False)
