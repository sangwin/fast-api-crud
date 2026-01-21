from fastapi import APIRouter
from app.models import User
from app.database import users_db

router = APIRouter()

@router.post("/users")
def create_user(user: User):
    user_dict = user.dict()
    user_dict["id"] = len(users_db) + 1
    users_db.append(user_dict)
    return user_dict

@router.get("/users")
def get_users():
    return users_db

@router.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}

@router.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            users_db[index].update(updated_user.dict())
            return users_db[index]
    return {"error": "User not found"}

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            users_db.pop(index)
            return {"message": "User deleted successfully"}
    return {"error": "User not found"}
