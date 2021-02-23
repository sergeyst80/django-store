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
    
    path('dictionaries/authors-list/', views.AuthorsList.as_view(), name='authors-list'),
    path('dictionaries/genres-list/', views.GenresList.as_view(), name='genres-list'),
    path('dictionaries/series-list/', views.SeriesList.as_view(), name='series-list'),
    path('dictionaries/publishers-list/', views.PublishersList.as_view(), name='publishers-list'),

    path('dictionaries/authors-delete/<int:pk>/', views.AuthorsDelete.as_view(), name='authors-delete'),
    path('dictionaries/genres-delete/<int:pk>/', views.GenresDelete.as_view(), name='genres-delete'),
    path('dictionaries/series-delete/<int:pk>/', views.SeriesDelete.as_view(), name='series-delete'),
    path('dictionaries/publishers-delete/<int:pk>/', views.PublishersDelete.as_view(), name='publishers-delete'),
    
    path('dictionaries/authors-update/<int:pk>/', views.AuthorsUpdate.as_view(), name='authors-update'),
    path('dictionaries/genres-update/<int:pk>/', views.GenresUpdate.as_view(), name='genres-update'),
    path('dictionaries/series-update/<int:pk>/', views.SeriesUpdate.as_view(), name='series-update'),
    path('dictionaries/publishes-update/<int:pk>/', views.PublishersUpdate.as_view(), name='publishers-update'),
    
    path('dictionaries/authors-create/', views.AuthorsCreate.as_view(), name='authors-create'),
    path('dictionaries/genres-create/', views.GenresCreate.as_view(), name='genres-create'),
    path('dictionaries/series-create/', views.SeriesCreate.as_view(), name='series-create'),
    path('dictionaries/publishers-create/', views.PublishersCreate.as_view(), name='publishers-create')
]
