from fastapi import FastAPI
from app.routes.user_routes import router as user_router

app = FastAPI(
    title="FastAPI MongoDB CRUD App",
    description="Simple CRUD application using FastAPI and MongoDB",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "FastAPI MongoDB CRUD API is running"
    }


app.include_router(user_router)