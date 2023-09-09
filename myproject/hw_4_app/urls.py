from django.urls import path

from . import views

app_name = 'hw_4_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('customer/<int:pk>/', views.CustomerView.as_view(), name='customer_page'),
    path('product/<int:pk>/', views.ProductView.as_view(), name='product_page'),
    path('update_product/<int:pk>/', views.UpdateProductView.as_view(), name='update_product'),
]