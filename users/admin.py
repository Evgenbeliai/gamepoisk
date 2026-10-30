from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users


@admin.register(Users)
class UsersAdmin(UserAdmin):
    # Колонки в списке пользователей
    list_display = ('username', 'email', 'comment_come', 'last_visit', 'is_staff', 'is_active')
    list_display_links = ('username',)

    # last_visit заполняется автоматически (auto_now=True),
    # поэтому вручную его менять нельзя — только смотреть
    readonly_fields = ('last_visit', 'last_login', 'date_joined')

    # Страница СОЗДАНИЯ пользователя
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Профиль', {'fields': ('email', 'avatar', 'bio')}),
    )