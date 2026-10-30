from .views import *
from django.urls import path
urlpatterns = [
    path('/regists', regist, name='regists')
]
