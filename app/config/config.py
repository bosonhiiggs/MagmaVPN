import os
from os import getenv

from dotenv import load_dotenv

"""
Файл загрузки параметров конфигурации приложения из файла .env.
"""
dotenv_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = getenv('SECRET_KEY', '664505b29bc6e76d9d306abfec05d1861b876ab98ff0bac84e002581036d2640')
ALGORITHM = getenv('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = getenv('ACCESS_TOKEN_EXPIRE_MINUTES', '30')

DB_HOST = getenv('DB_HOST', 'mongodb://localhost:27017/')

