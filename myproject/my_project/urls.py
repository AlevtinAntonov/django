"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('les3/', include('myapp3.urls')),
    path('les4/', include('myapp4.urls')),
    path('hw/', include('hw_1_app.urls')),
    path('hw2/', include('hw_2_app.urls')),
    path('hw3/', include('hw_3_app.urls')),
    path('s1/', include('s1app.urls')),
    path('s2/', include('s2app.urls')),
    path('s3/', include('s3app.urls')),
    path('s4/', include('seminar_app.urls')),
]
