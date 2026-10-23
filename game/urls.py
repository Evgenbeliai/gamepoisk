from django.urls import path
from .views import *
urlpatterns = [
    path('', start, name = 'start'),
    path('<int:gameid>/', gameinf, name = 'gameinf')
]