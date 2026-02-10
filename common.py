from fastapi import APIRouter

router = APIRouter()

from utils.validation import validate_data, validate_id
from models.user import User

@router.post("/users/")
async def create_user(user_data: dict):
    validated_user = validate_data(user_data, User)
    # Create the user
    return validated_user

@router.get("/users/{user_id}")
async def read_user(user_id: int):
    validated_id = validate_id(user_id)
    # Get the user with the validated ID
    return user_id