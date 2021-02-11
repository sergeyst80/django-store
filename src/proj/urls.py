"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from dictionaries import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dict_view, name='dict-view'),
    path('dict-detail/<int:pk>/', views.dict_detail, name='dict-detail'),
    path('dict-update/<int:pk>/', views.dict_update, name='dict-update'),
    path('dict-delete/<int:pk>/', views.dict_delete, name='dict-delete'),
    path('dict-add/', views.dict_add, name='dict-add'),
    path('dict-update/<int:pk>/', views.dict_update, name='dict-update')
]
