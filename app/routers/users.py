from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.models import UserBase, UserCreate, UserResponse
from app.database import users_db
from app.auth import get_current_user, hash_password

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserCreate):
    """
    Create a new user
    """

    if any(existing["email"] == user.email for existing in users_db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    new_id = max([u["id"] for u in users_db], default=0) + 1

    new_user = {
        "id": new_id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "password": hash_password(user.password)
    }

    users_db.append(new_user)

    return {
        "id": new_user["id"],
        "name": new_user["name"],
        "email": new_user["email"],
        "age": new_user["age"]
    }


@router.get("",response_model=List[UserBase], dependencies=[Depends(get_current_user)])
def get_users():
    """
    Get all users (protected)
    """
    return users_db


@router.get("/{user_id}", dependencies=[Depends(get_current_user)])
def get_user(user_id: int):
    """
    Get user by ID (protected)
    """
    for user in users_db:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )
