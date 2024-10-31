from fastapi.testclient import TestClient
from mgibert_conta_py.app.main import app


client = TestClient(app)


def test_when_create_project_should_return_201():
    # Given:
    new_project_data = {
        "key": "project_acceptance_test_creation",
        "description": "This project is created for testing purposes",
        "period": "24-25"
    }

    # When:
    response = client.post("/projects", json=new_project_data)

    # tHen
    assert response.status_code == 201

    created_project = response.json()
    assert created_project["project_id"] is not None
    assert created_project["key"] == "project_acceptance_test_creation"
    assert created_project["description"] == "This project is created for testing purposes"
    assert created_project["period"] == "24-25"
