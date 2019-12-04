# Findee Server API
Для запуска требуется в одной папке с файлом requirements.txt прописать команду:
```bash 
pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
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
    * birth_date: дата рождения. String. в формате ГГГГ-ММ-ДД
    * kind: класс ("client" или "specialist"). String
    * regions: регион(-ы). String
    * phone: номер телефона. String
    * company?: организация. String | ДЛЯ СПЕЦИАЛИСТОВ
    * categories?: категории. String | ДЛЯ СПЕЦИАЛИСТОВ
* resp:
    * name: имя пользователя. String
    * surname: фамилия. String
    * patronymic: отчество. String
    * birth_date: дата рождения. String. в формате ГГГГ-ММ-ДД
    * kind: класс ("client" или "specialist"). String
    * regions: регион(-ы). String
    * phone: номер телефона. String
    * company: организация. String (null для пользователей с kind == "client")
    * categories: категории. String (null для пользователей с kind == "client")


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
    * birth_date: дата рождения. String. в формате ГГГГ-ММ-ДД
    * photo: аватарка пользователя. Url
    * kind: класс ("client" или "specialist"). String
    * regions: регион(-ы). String
    * phone: номер телефона. String
    * company: организация. String (null для пользователей с kind == "client")
    * categories: категории. String (null для пользователей с kind == "client")
    * about: о себе. String
    * images: картинки в портфолио
        * id: id картинки. Number
        * image: ссылка на саму картинку. Url
        * text: описание картинки. String 
    * verify: верификация личности. Boolean (всегда false для пользователей с kind == "client")
    * premium: наличие премиум-аккаунта. Boolean (всегда false для пользователей с kind == "client") 


**5) PATCH /profile/int:user_id/update** Изменение профиля пользователя
* req:
    > Если пользователь неверифицирован доступны такие данные для изменения:

    * name?: имя пользователя. String
    * surname?: фамилия. String
    * patronymic?: отчество. String
    * birth_date?: дата рождения. String. в формате ГГГГ-ММ-ДД
    * photo?: аватарка пользователя. File (image)
    * kind?: класс ("client" или "specialist"). String
    * regions?: регион(-ы). String
    * phone?: номер телефона. String
    * company?: организация. String | ДЛЯ СПЕЦИАЛИСТОВ
    * categories?: категории. String | ДЛЯ СПЕЦИАЛИСТОВ
    * about?: о себе. String
    * images?: картинки в портфолио
        * id: id картинки. Number
        * image: ссылка на саму картинку. Url
        * text: описание картинки. String 

    > Если пользователь верифицирован запрещено изменять ФИО и дату рождения
* resp:
    * user:
        * id: id пользователя. Number
        * username: почта пользователя (логин). String
    * name: имя пользователя. String
    * surname: фамилия. String
    * patronymic: отчество. String
    * birth_date: дата рождения. String. в формате ГГГГ-ММ-ДД
    * photo: аватарка пользователя. Url
    * kind: класс ("client" или "specialist"). String
    * regions: регион(-ы). String
    * phone: номер телефона. String
    * company: организация. String (null для пользователей с kind == "client")
    * categories: категории. String (null для пользователей с kind == "client")
    * about: о себе. String
    * images: картинки в портфолио
        * id: id картинки. Number
        * image: ссылка на саму картинку. Url
        * text: описание картинки. String 
    * verify: верификация личности. Boolean (всегда false для пользователей с kind == "client")
    * premium: наличие премиум-аккаунта. Boolean (всегда false для пользователей с kind == "client")  


**6) POST /image/create** Создание картинки в портфолио специалиста
* req:
    * image: сама картинка. File (image)
    * text: описание картинки. String
* resp:
    * id: id картинки. Number
    * image: ссылка на саму картинку. Url
    * text: описание картинки. String


**7) GET /image/int:id** Получение данных о картинки в портфолио
* req:
    * -
* resp:
    * id: id картинки. Number
    * image: ссылка на саму картинку. Url
    * text: описание картинки. String


**8) PATCH /image/int:id/update** Обновление картинки в портфолио
* req:
    * image?: сама картинка. File (image)
    * text?: описание картинки. String
* resp:
    * id: id картинки. Number
    * image: ссылка на саму картинку. Url
    * text: описание картинки. String


**8) DELETE /image/int:id/delete** Удаление картинки в портфолио
* req:
    * -
* resp:
    * -