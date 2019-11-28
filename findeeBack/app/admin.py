from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Юзер',             {'fields': ['user']}),
        ('Главное',          {'fields': ['name', 'surname', 'patronymic', 'kind']}),
        ('Контакты',         {'fields': ['regions', 'phone']}),
        ('ДЛЯ СПЕЦИАЛИСТОВ', {'fields': ['company', 'categories']}),
    ]

admin.site.register(Profile, ProfileAdmin)
