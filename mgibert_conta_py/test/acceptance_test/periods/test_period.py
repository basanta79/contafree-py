import pytest
from fastapi.testclient import TestClient
from mgibert_conta_py.app.main import app


client = TestClient(app)


def test_when_create_period_should_return_201():
    # Given:
    new_period_data = {
        "period_name": "24-25"
    }

    # When:
    response = client.post("/periods", json=new_period_data)

    # tHen
    assert response.status_code == 201

    created_period = response.json()
    assert created_period["period_name"] == "24-25"
    period_id = created_period["period_id"]
