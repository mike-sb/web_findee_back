# Findee Back-End Django + Django Rest API

    POST /register "Регистрация пользователя"    
        req: {
            "username": "почта пользователя (логин), string",
            "password": "пароль, string"
        }
        resp: {
            "user": {
                "id": "айди из БД, number",
                "username": "почта пользователя, string"
            },
            "token-access": "токен, string"
        }


    POST /login "Авторизация пользователя"
        req: {
            "username": "почта пользователя (логин), string",
            "password": "пароль пользователя, string"
        }
        resp: {
            "user": {
                "id": "айди из БД, number",
                "username": "логин пользователя (почта), string"
            }
        },
        "token-access": "токен, string"
