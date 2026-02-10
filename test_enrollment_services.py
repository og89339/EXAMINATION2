from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_enrollment():
    response = client.post("/enrollments/", json={"id": 0, "user_id": 1, "course_id": 1})
    assert response.status_code == 200
    assert response.json()["id"] >0

def test_get_enrollments():
    response = client.get("/enrollments/")
    assert response.status_code == 200

def test_get_enrollment():
    response = client.get("/enrollments/1")
    assert response.status_code == 200
    assert response.json()["id"] >0

def delete_enrollment(db: test_get_enrollment, enrollment_id: int):
    db_enrollment = db.query(delete_enrollment).filter(delete_enrollment.id == enrollment_id).first()
    db.delete(db_enrollment)
    db.commit()
    return {"message": "enrollment deleted successfully"}
