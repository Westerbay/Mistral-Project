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

def test_request_with_default_model(client):
    response = client.post("/request", json={"prompt": "Hello", "model": "AIModel"})
    assert response.status_code == 200
    data = response.json()
    assert "text" in data
