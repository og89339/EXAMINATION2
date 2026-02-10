import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"id": 0, "name": "akinlade rilwan", "email": "ogadekule@gmail.com", "role": "student"})
    assert response.status_code == 200
    assert response.json()["id"] >0
    assert response.json()["name"] == "akinlade rilwan"
    assert response.json()["email"] == "ogadekule@gmail.com"
    assert response.json()["role"] == "student"

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] >0
    assert response.json()["name"] == "akinlade rilwan"
    assert response.json()["email"] == "ogadekule@gmail.com"
    assert response.json()["role"] == "student"