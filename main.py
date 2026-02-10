from fastapi import FastAPI
from routes.users import router as users_router
from routes.courses import router as courses_router
from routes.enrollments import router as enrollments_router

app = FastAPI()

app.include_router(users_router)
app.include_router(courses_router)
app.include_router(enrollments_router)