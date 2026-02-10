from fastapi import APIRouter, HTTPException
from models.user import User, UserCreate

router = APIRouter()

# In-memory data store
users = [
    User(id=1, name="akinlade rilwan", email="ogadekule@gmail.com", role="student"),
    User(id=2, name="akinlade rilwan", email="ogadekule@gmail.com", role="admin"),
]

@router.post("/users/", response_model=User)
def create_user(user: UserCreate):
    new_user_id = len(users) + 1
    new_user = User(id=new_user_id, **user.model_dump())
    users.append(new_user)
    return new_user

@router.get("/users/", response_model=list[User])
def read_users():
    return users

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
