from bson import ObjectId
from fastapi import HTTPException
from app.database import user_collection
from app.models.user_model import user_serializer, users_serializer


def create_user_service(user_data: dict):
    existing_user = user_collection.find_one({"email": user_data["email"]})

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    result = user_collection.insert_one(user_data)

    created_user = user_collection.find_one({"_id": result.inserted_id})

    return user_serializer(created_user)


def get_all_users_service():
    users = user_collection.find()
    return users_serializer(users)


def get_user_by_id_service(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user id")

    user = user_collection.find_one({"_id": ObjectId(user_id)})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user_serializer(user)


def update_user_service(user_id: str, update_data: dict):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user id")

    update_data = {key: value for key, value in update_data.items() if value is not None}

    if not update_data:
        raise HTTPException(status_code=400, detail="No data provided for update")

    user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    updated_user = user_collection.find_one({"_id": ObjectId(user_id)})

    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")

    return user_serializer(updated_user)


def delete_user_service(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user id")

    deleted_user = user_collection.find_one_and_delete({"_id": ObjectId(user_id)})

    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")

    return user_serializer(deleted_user)