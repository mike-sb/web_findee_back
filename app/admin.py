from django.contrib import admin

from .models import Profile, Image, Rating, Comment

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fk_name = "to_profile"


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Юзер',             {'fields': ['user', 'verify', 'premium']}),
        ('Главное',          {'fields': ['name', 'surname', 'patronymic', 'birth_date', 'photo', 'kind']}),
        ('Дополнительно',    {'fields': ['about']}),
        ('Контакты',         {'fields': ['regions', 'phone']}),
        ('ДЛЯ СПЕЦИАЛИСТОВ', {'fields': ['company', 'categories']}),
    ]
    inlines = [ImageInline, RatingInline, CommentInline]

admin.site.register(Profile, ProfileAdmin)
