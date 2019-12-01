# Findee Server API
Для запуска требуется в одной папке с файлом requirements.txt прописать команду:
```bash 
pip install -r requirements.txt
```

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
* resp:
  * user
      * id: id пользователя. Number
      * username: почта пользователя (логин). String
      * token-access: токен аутентификации. String


**3) POST /profile/create** Создание профиля пользователя
* req:
  * name: имя пользователя. String
  * surname: фамилия. String
  * patronymic: отчество. String
  * kind: класс ("client" или "specialist"). String
  * regions: регион(-ы). String
  * phone: номер телефона. String
  * company?: организация. String | ДЛЯ СПЕЦИАЛИСТОВ
  * categories?: категории. String | ДЛЯ СПЕЦИАЛИСТОВ
* resp:
    * name: имя пользователя. String
    * surname: фамилия. String
    * patronymic: отчество. String
    * kind: класс ("client" или "specialist"). String
    * regions: регион(-ы). String
    * phone: номер телефона. String
    * company: организация. String (null для пользователей с kind == "client")
    * categories: категории. String (null для пользователей с kind == "client")
    * verify: верификация личности. Boolean (всегда false для пользователей с kind == "client")  


**4) GET /profile/int:user_id/** Данные о профиле пользователя
* req:
    * -
* resp:
    * user 
        * id: id пользователя. Number
        * username: почта пользователя (логин). String
    * name: имя пользователя. String
    * surname: фамилия. String
    * patronymic: отчество. String
    * kind: класс ("client" или "specialist"). String
    * regions: регион(-ы). String
    * phone: номер телефона. String
    * company: организация. String (null для пользователей с kind == "client")
    * categories: категории. String (null для пользователей с kind == "client")
    * verify: верификация личности. Boolean (всегда false для пользователей с kind == "client")  


**5) PATCH | PUT /profile/int:user_id/update** Изменение профиля пользователя
* req:
    > Если пользователь неверифицирован доступны такие данные для изменения:
    * name?: имя пользователя. String
    * surname?: фамилия. String
    * patronymic?: отчество. String
    * kind?: класс ("client" или "specialist"). String
    * regions?: регион(-ы). String
    * phone?: номер телефона. String
    * company?: организация. String | ДЛЯ СПЕЦИАЛИСТОВ
    * categories?: категории. String | ДЛЯ СПЕЦИАЛИСТОВ

    > Если пользователь верифицирован запрещено изменять ФИО
* resp:
    * user:
        * id: id пользователя. Number
        * username: почта пользователя (логин). String
    * name: имя пользователя. String
    * surname: фамилия. String
    * patronymic: отчество. String
    * kind: класс ("client" или "specialist"). String
    * regions: регион(-ы). String
    * phone: номер телефона. String
    * company: организация. String (null для пользователей с kind == "client")
    * categories: категории. String (null для пользователей с kind == "client")
    * verify: верификация личности. Boolean (всегда false для пользователей с kind == "client")  