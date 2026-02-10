import pytest
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_create_course():
    response = client.post("/courses/", json={"id": 0, "title": "backend", "code": "PYTHON"})
    assert response.status_code == 200
    assert response.json()["id"] >0
    assert response.json()["title"] == "backend"
    assert response.json()["code"] == "PYTHON"

def test_get_courses():
    response = client.get("/courses/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_course():
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert response.json()["id"] >0
    assert response.json()["title"] == "backend"
    assert response.json()["code"] == "PYTHON"