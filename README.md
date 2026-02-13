Course Enrollment Management API
This is a RESTful API built using FastAPI that manages course enrollments. It supports public access to course information, user-based roles, and role-based restrictions on certain operations.

Running the APITo run the API, navigate to the project directory and use the following command:

bash
uvicorn main:app --reload

install pytest
pip install pytest

Running Tests To run the tests and services, use the following command:

bash
python -m pytest tests or services

To run the models and routes

curl http://localhost:8000/users/ or http://127.0.0.1:8000 
curl http://localhost:8000/users/1 or http://127.0.0.1:8000 

curl http://localhost:8000/courses/ or http://127.0.0.1:8000 
curl http://localhost:8000/courses/1 or http://127.0.0.1:8000 

curl http://localhost:8000/enrollments/ or http://127.0.0.1:8000 
curl http://localhost:8000/enrollments/1 or http://127.0.0.1:8000 

To run the util
python -m unittest discover

To check if all the test work
python -m pytest

ThE StRuCtUe Of ThE CoDe 

project/
|---- main.py
|---- models/
|       |---- user.py
|       |---- course.py
|       |---- enrollment.py
|---- routes/
|       |---- users.py
|       |---- courses.py
|       |---- enrollments.py
|---- services/
|       |---- test_user_service.py
|       |---- test_course_service.py
|       |---- test_enrollment_service.py
|---- tests/
|       |---- test_users.py
|       |---- test_courses.py
|   |----test_enrollments.py

|---- utils/
|       |---- validation.py
        |---- common.py 
|---- requirements.txt
|---- README.md
