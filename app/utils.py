from datetime import timedelta, datetime, timezone

import jwt
from passlib.context import CryptContext

from app.database.serializers import user_entity
from .config.config import SECRET_KEY, ALGORITHM
from .database.database import collection_name

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


# Функция проверки пароля
def get_hashed_password(password: str) -> str:
    return pwd_context.hash(password)


# Функция проверки пароля
def verify_password(enter_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(enter_password, hashed_password)


# Функция входа
def get_user_data(username: str):
    user_data = collection_name.find_one({"username": username})
    if not user_data:
        return None
    return user_data


# Функция авторизации
def authenticate_user(username: str, password: str) -> bool | dict:
    user = get_user_data(username=username)
    if not user:
        return False
    if not verify_password(password, user['password']):
        return False
    return user_entity(user)


# Создание ACCESS токена для авторизации
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
