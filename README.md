# Findee Server API
Для запуска требуется в одной папке с файлом requirements.txt прописать команду:
> pip install -r requirements.txt


**1) POST /register** Регистрация пользователя
* req:
  * username: почта пользователя (логин). String
  * password: пароль пользователя. String
* resp:
  * user
    * id: id пользователя. Number
    * username: почта пользователя (логин). String
    * token-access: токен аутентификации. String

**2) GET /login** Авторизация пользователя
* req:
  * username: почта пользователя (логин). String
  * password: пароль пользователя. String
* resp
  * user
      * id: id пользователя. Number
      * username: почта пользователя (логин). String
      * token-access: токен аутентификации. String
