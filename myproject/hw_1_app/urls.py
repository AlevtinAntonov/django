from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='hw'),
    path('home_task/', views.home_task, name='home_task'),
]