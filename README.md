# Findee Server API

**POST /register** Регистрация пользователя
* req:
  * username: почта пользователя (логин). String
  * password: пароль пользователя. String
* resp:
  * user
    * id: id пользователя. Number
    * username: почта пользователя (логин). String
    * token-access: токен аутентификации. String

**POST /login** Авторизация пользователя
* req:
  * username: почта пользователя (логин). String
  * password: пароль пользователя. String
* resp
  * user
      * id: id пользователя. Number
      * username: почта пользователя (логин). String
      * token-access: токен аутентификации. String
