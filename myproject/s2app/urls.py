from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='hw'),
    path('heads/', views.head_tails, name='head_tails'),
]