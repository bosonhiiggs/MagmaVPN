from pydantic import BaseModel


# Модель пользователя
class User(BaseModel):
    username: str
    password: str
