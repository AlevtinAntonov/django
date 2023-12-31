from django.urls import path

from hw_2_app import views

app_name = 'hw_2_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
]