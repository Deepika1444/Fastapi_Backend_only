from fastapi import APIRouter
from app.schemas.user_schema import UserCreate, UserUpdate
from app.services.user_service import (
    create_user_service,
    get_all_users_service,
    get_user_by_id_service,
    update_user_service,
    delete_user_service
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
def create_user(user: UserCreate):
    created_user = create_user_service(user.dict())
    print("Created user response:", created_user)

    return {
        "message": "User created successfully",
        "data": created_user
    }


@router.get("/")
def get_all_users():
    users = get_all_users_service()

    return {
        "message": "Users fetched successfully",
        "data": users
    }


@router.get("/{user_id}")
def get_user_by_id(user_id: str):
    user = get_user_by_id_service(user_id)

    return {
        "message": "User fetched successfully",
        "data": user
    }


@router.put("/{user_id}")
def update_user(user_id: str, user: UserUpdate):
    updated_user = update_user_service(user_id, user.dict())

    return {
        "message": "User updated successfully",
        "data": updated_user
    }


@router.delete("/{user_id}")
def delete_user(user_id: str):
    deleted_user = delete_user_service(user_id)

    return {
        "message": "User deleted successfully",
        "data": deleted_user
    }