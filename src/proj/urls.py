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
from dictionaries import views, models


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_dicts, name='dicts-list'),
    path('authors-list/', views.AuthorsList.as_view(), name='authors-list'),
    path('countries-list/', views.CountriesList.as_view(), name='countries-list'),
    path('authors-detail/<int:pk>/', views.AuthorsDetail.as_view(), name='authors-detail'),
    path('authors-delete/<int:pk>/', views.AuthorsDelete.as_view(), name='authors-delete'),
    path('countries-delete/<int:pk>/', views.CountriesDelete.as_view(), name='countries-delete'),
    path('authors-update/<int:pk>/', views.AuthorsUpdate.as_view(), name='authors-update'),
    path('countries-update/<int:pk>/', views.CountriesUpdate.as_view(), name='countries-update'),
    path('authors-create/', views.AuthorsCreate.as_view(), name='authors-create'),
    path('countries-create/', views.CountriesCreate.as_view(), name='countries-create')
]
