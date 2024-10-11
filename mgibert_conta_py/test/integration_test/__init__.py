import contextlib

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os


DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql://pablo:example@localhost:5433/treasury_test")


engine = create_engine(
    DATABASE_URL,
    pool_size=20,  # Max connections in the pool
    max_overflow=10,  # overhead of connections id the pool runs out
    pool_timeout=30,  # Timeout to reject connection
    pool_recycle=1800  # Lifetime of a connection in sec
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

@pytest.fixture
def storage():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
