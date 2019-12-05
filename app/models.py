from django.db import models
from django.contrib.auth.models import User

from .choices import CATEGORIES, KIND_CHOICES


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", related_name="profile", on_delete=models.CASCADE)
    name = models.CharField("Имя", max_length=30)
    surname = models.CharField("Фамилия", max_length=30)
    patronymic = models.CharField("Отчество", max_length=30)
    birth_date = models.DateField("Дата рождения")
    photo = models.ImageField("Главное фото", upload_to="profile_photo/%Y/%m/%d", default="default.jpg")
    kind = models.CharField("Клиент или специалист", max_length=20, choices=KIND_CHOICES)
    regions = models.CharField("Регионы", max_length=100)
    phone = models.CharField("Телефон", max_length=15)

    # Дополнительно
    about = models.TextField("О себе", blank=True)

    # Для специалистов
    verify = models.BooleanField("Верифицирован", default=False)
    premium = models.BooleanField("Премиум аккаунт", default=False)
    company = models.CharField("Организация", max_length=100, null=True, blank=True)
    categories = models.CharField("Направления", blank=True, null=True, max_length=200, choices=CATEGORIES)

    def __str__(self):
        return "Профиль " + self.user.username 

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class Image(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="images", 
        verbose_name="Профиль", blank=True, null=True
    )
    text = models.TextField("Описание фотографии", blank=True, null=True)
    image = models.ImageField("Фотография", upload_to="portfolio_images/%Y/%m/%d")

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class Rating(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="rating", 
        verbose_name="Рейтинг", blank=True, null=True
    )
    rating = models.IntegerField()

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"