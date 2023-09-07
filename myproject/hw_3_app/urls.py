from django.urls import path

from hw_3_app import views

from hw_3_app.views import ProductsFromOrders

app_name = 'hw_3_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('clients/', views.clients, name='clients'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('product_orders/<int:pk>', ProductsFromOrders.as_view(), name='products_orders')
]