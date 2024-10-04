import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PeriodModel(Base):
    __tablename__ = "periods"

    period_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    period_name = Column("period", String, nullable=False)
