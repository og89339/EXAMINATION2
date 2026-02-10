from fastapi import APIRouter, HTTPException
from models.course import Course, CourseCreate

router = APIRouter()

# In-memory data store
courses = [
    Course(id=1, title="backend", code="PYTHON"),
    Course(id=2, title="frontend", code="HTML&CSS"),
]

@router.post("/courses/", response_model=Course)
def create_course(course: CourseCreate):
    new_course_id = len(courses) + 1
    new_course = Course(id=new_course_id, **course.model_dump())
    courses.append(new_course)
    return new_course

@router.get("/courses/", response_model=list[Course])
def read_courses():
    return courses

@router.get("/courses/{course_id}", response_model=Course)
def read_course(course_id: int):
    for course in courses:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=404, detail="Course not found")


