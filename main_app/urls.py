"""Define URL patterns for main_app"""

from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    # Головна сторінка
    path('', views.index, name='index'),
]
