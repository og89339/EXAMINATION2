from fastapi import HTTPException
from pydantic import ValidationError

def validate_data(data, model):
    try:
        return model(**data)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())

def validate_id(id):
    if not isinstance(id, int) or id < 1:
        raise HTTPException(status_code=400, detail="Invalid ID")
    return id