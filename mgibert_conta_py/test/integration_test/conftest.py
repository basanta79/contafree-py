import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session


def pytest_collection_modifyitems(items):
    for item in items:
        if "integration" in item.nodeid:
            item.add_marker(pytest.mark.integration)

@pytest.fixture(scope="function", autouse=True)
def clean_db_after_test(storage: Session):
    yield
    storage.execute(text('TRUNCATE TABLE periods RESTART IDENTITY CASCADE'))
    storage.commit()
