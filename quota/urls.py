# from unicodedata import name
from django.urls import path

from . import views

app_name = 'quotas'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:quota_id>', views.quota, name='quota'),
]