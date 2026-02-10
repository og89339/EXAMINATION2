import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_enrollment():
    response = client.post("/enrollments/", json={"id": 0, "user_id": 1, "course_id": 1})
    assert response.status_code == 200
    assert response.json()["id"] >0
    assert response.json()["user_id"] == 1
    assert response.json()["course_id"] == 1
    


def test_get_enrollments():
    response = client.get("/enrollments/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_enrollment():
    response = client.get("/enrollments/1")
    assert response.status_code == 200
    assert response.json()["id"] >0
    assert response.json()["user_id"] == 1
    assert response.json()["course_id"] == 1
    
    