from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    role: str

class UserCreate(BaseModel):
    name: str
    email: str
    role: str