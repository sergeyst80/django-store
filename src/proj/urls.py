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
from django.conf import settings
from django.conf.urls.static import static

from dictionaries import views as dicts_views
from mainapp import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', main_views.HomePage.as_view(), name='homepage'),

    path('dictionaries/authors-list/', dicts_views.AuthorsList.as_view(), name='authors-list'),
    path('dictionaries/genres-list/', dicts_views.GenresList.as_view(), name='genres-list'),
    path('dictionaries/series-list/', dicts_views.SeriesList.as_view(), name='series-list'),
    path('dictionaries/publishers-list/', dicts_views.PublishersList.as_view(), name='publishers-list'),
    path('dictionaries/age_categories-list/', dicts_views.AgeCategoriesList.as_view(), name='age_categories-list'),
    path('dictionaries/book_formats-list/', dicts_views.BookFormatsList.as_view(), name='book_formats-list'),

    path('dictionaries/authors-delete/<int:pk>/', dicts_views.AuthorsDelete.as_view(), name='authors-delete'),
    path('dictionaries/genres-delete/<int:pk>/', dicts_views.GenresDelete.as_view(), name='genres-delete'),
    path('dictionaries/series-delete/<int:pk>/', dicts_views.SeriesDelete.as_view(), name='series-delete'),
    path('dictionaries/publishers-delete/<int:pk>/', dicts_views.PublishersDelete.as_view(), name='publishers-delete'),
    path('dictionaries/age_categories-delete/<int:pk>/', dicts_views.AgeCategoriesDelete.as_view(), name='age_categories-delete'),
    path('dictionaries/book_formats-delete/<int:pk>/', dicts_views.BookFormatsDelete.as_view(), name='book_formats-delete'),
    
    path('dictionaries/authors-update/<int:pk>/', dicts_views.AuthorsUpdate.as_view(), name='authors-update'),
    path('dictionaries/genres-update/<int:pk>/', dicts_views.GenresUpdate.as_view(), name='genres-update'),
    path('dictionaries/series-update/<int:pk>/', dicts_views.SeriesUpdate.as_view(), name='series-update'),
    path('dictionaries/publishes-update/<int:pk>/', dicts_views.PublishersUpdate.as_view(), name='publishers-update'),
    path('dictionaries/age_categories-update/<int:pk>/', dicts_views.AgeCategoriesUpdate.as_view(), name='age_categories-update'),
    path('dictionaries/book_formats-update/<int:pk>/', dicts_views.BookFormatsUpdate.as_view(), name='book_formats-update'),
    
    path('dictionaries/authors-create/', dicts_views.AuthorsCreate.as_view(), name='authors-create'),
    path('dictionaries/genres-create/', dicts_views.GenresCreate.as_view(), name='genres-create'),
    path('dictionaries/series-create/', dicts_views.SeriesCreate.as_view(), name='series-create'),
    path('dictionaries/publishers-create/', dicts_views.PublishersCreate.as_view(), name='publishers-create'),
    path('dictionaries/age_categories-create/', dicts_views.AgeCategoriesCreate.as_view(), name='age_categories-create'),
    path('dictionaries/book_formats-create/', dicts_views.BookFormatsCreate.as_view(), name='book_formats-create')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)