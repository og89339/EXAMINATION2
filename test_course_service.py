from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_course():
    response = client.post("/courses/", json={"id": 0, "title": "backend", "code": "PYTHON"})
    assert response.status_code == 200
    assert response.json()["id"] >0

def test_get_courses():
    response = client.get("/courses/")
    assert response.status_code == 200

def test_get_course():
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert response.json()["id"] >0

def delete_course(db: test_get_course, course_id: int):
    db_course = db.query(delete_course).filter(delete_course.id == course_id).first()
    db.delete(db_course)
    db.commit()
    return {"message": "Course deleted successfully"}