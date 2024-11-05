from pymongo.mongo_client import MongoClient


# Ссылка на сервер MongoDB
uri = "mongodb://localhost:27017/"
# Объект кластера базы данных
client = MongoClient(uri)

# Клиент подключения базы данных
db = client.mangavpn_db
# Коллекция с пользователями
collection_name = db['users_collection']
