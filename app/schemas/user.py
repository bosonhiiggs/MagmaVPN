from pydantic import BaseModel


# Модель пользователя
class User(BaseModel):
    username: str


class UserInDB(User):
    hashed_password: str


class UserCreate(User):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
