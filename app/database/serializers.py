# Схема получения пользователя
def user_entity(user_item) -> dict:
    return {
        'id': str(user_item['_id']),
        'name': str(user_item['username']),
    }


# Схема получения списка получения пользователей
def list_users_entity(users) -> list:
    return [user_entity(user) for user in users]
