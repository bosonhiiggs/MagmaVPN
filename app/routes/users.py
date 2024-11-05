from fastapi import APIRouter

from ..database.database import collection_name
from ..database.models import User
from ..database.schemas import list_users

router = APIRouter()


# Путь для получения списка пользователей
@router.get("/users/")
async def get_users():
    users = list_users(collection_name.find())
    return users


# Путь для создания пользователя
@router.post("/users/")
async def post_user(user: User):
    collection_name.insert_one(dict(user))

