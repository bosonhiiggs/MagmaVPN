from fastapi import FastAPI
from .routes.users import router

# Создание объекта фреймворка
app = FastAPI()


# Подключение путей приложения
app.include_router(router)
