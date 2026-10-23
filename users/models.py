from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, verbose_name='Аватар')
    bio = models.TextField(blank=True, verbose_name="О себе")
    comment_come = models.IntegerField(default=0, verbose_name="Количество оценок")
    last_visit = models.DateTimeField(auto_now=True, verbose_name='Последний заход')
    is_staff = models.BooleanField(default=False, verbose_name='Доступ к админ панеле ')
    is_superuser = models.BooleanField(default=False, verbose_name='полный доступ')
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
# Create your models here.
