from datetime import timedelta

from fastapi import APIRouter, Response, status

from ..config.config import ACCESS_TOKEN_EXPIRE_MINUTES
from ..database.database import collection_name
from ..schemas.user import UserCreate, Token
from app.database.serializers import list_users_entity
from ..utils import get_hashed_password, authenticate_user, create_access_token

router = APIRouter()


# Путь для получения списка пользователей
@router.get("/users/", status_code=status.HTTP_200_OK)
async def get_users():
    users = list_users_entity(collection_name.find())
    return users


# Путь для создания пользователя
@router.post("/users/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, response: Response):
    user_data = collection_name.find_one({"username": user.username})
    if user_data is None:
        hashed_password = get_hashed_password(user.password)
        user.password = hashed_password
        collection_name.insert_one(dict(user))
        return user
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"error": "User already exists"}


# Путь входа
@router.post("/users/login/", status_code=status.HTTP_200_OK)
async def login_user(user: UserCreate, response: Response):
    auth_user = authenticate_user(username=user.username, password=user.password)
    if not auth_user:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"error": "Invalid username or password"}
    # return auth_user

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
