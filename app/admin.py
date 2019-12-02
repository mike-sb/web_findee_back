from django.contrib import admin

from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Юзер',             {'fields': ['user', 'verify', 'premium']}),
        ('Главное',          {'fields': ['name', 'surname', 'patronymic', 'birth_date', 'photo', 'kind']}),
        ('Дополнительно',    {'fields': ['about']}),
        ('Контакты',         {'fields': ['regions', 'phone']}),
        ('ДЛЯ СПЕЦИАЛИСТОВ', {'fields': ['company', 'categories']}),
    ]

admin.site.register(Profile, ProfileAdmin)
