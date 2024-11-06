from pymongo.mongo_client import MongoClient

from app.config.config import DB_HOST

# Ссылка на сервер MongoDB
uri = DB_HOST
# Объект кластера базы данных
client = MongoClient(uri)

# Клиент подключения базы данных
db = client.mangavpn_db
# Коллекция с пользователями
collection_name = db['users_collection']
