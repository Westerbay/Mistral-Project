from fastapi.testclient import TestClient
from app import Application

import pytest


@pytest.fixture
def client():
    app = Application("mistral-large-latest", "", "localhost", 8000)
    client = TestClient(app.app)
    return client

def test_get_models(client):
    response = client.post("/get_models")
    assert response.status_code == 200
    data = response.json()
    assert "models" in data
    assert isinstance(data["models"], list)
    assert "AIModel" in data["models"]

def test_change_model_ok(client):
    response = client.post("/change_model", json={"model": "AIQuiz"})
    assert response.status_code == 200
    assert response.json()["status"] == "OK"

def test_change_model_ko(client):
    response = client.post("/change_model", json={"model": "FakeModel"})
    assert response.status_code == 200
    assert response.json()["status"] == "KO"

def test_request_with_default_model(client):
    response = client.post("/request", json={"prompt": "Hello"})
    assert response.status_code == 200
    data = response.json()
    assert "text" in data
