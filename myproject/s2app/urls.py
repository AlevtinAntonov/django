from django.urls import path

from s2app import views

app_name = 's2app'

urlpatterns = [
    path('', views.index, name='index'),
    path('last/', views.last_games, name='last_games'),
    path('author/', views.autor, name='author'),
]