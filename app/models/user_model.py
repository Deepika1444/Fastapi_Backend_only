def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age": user["age"]
    }


def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]