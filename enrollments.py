from fastapi import APIRouter, HTTPException
from models.enrollment import Enrollment, EnrollmentCreate

router = APIRouter()

# In-memory data store
enrollments = [
    Enrollment(id=1, user_id=1, course_id=1),
    Enrollment(id=2, user_id=2, course_id=2),
]

@router.post("/enrollments/", response_model=Enrollment)
def create_enrollment(enrollment: EnrollmentCreate):
    new_enrollment_id = len(enrollments) + 1
    new_enrollment = Enrollment(id=new_enrollment_id, **enrollment.model_dump())
    enrollments.append(new_enrollment)
    return new_enrollment

@router.get("/enrollments/", response_model=list[Enrollment])
def read_enrollments():
    return enrollments

@router.get("/enrollments/{enrollment_id}", response_model=Enrollment)
def read_enrollment(enrollment_id: int):
    for enrollment in enrollments:
        if enrollment.id == enrollment_id:
            return enrollment
    raise HTTPException(status_code=404, detail="Enrollment not found")

@router.delete("/enrollments/{enrollment_id}")
def delete_enrollment(enrollment_id: int):
    for enrollment in enrollments:
        if enrollment.id == enrollment_id:
            enrollments.remove(enrollment)
            return {"message": "Enrollment deleted successfully"}
    raise HTTPException(status_code=404, detail="Enrollment not found")

