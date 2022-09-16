# from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:quota_id>', views.quota, name='quota'),
]