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

from references import views as refs_views
from mainapp import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', main_views.HomePage.as_view(), name='homepage'),
    path('books-catalog', main_views.BooksCatalog.as_view(), name='books-catalog'),

    path('references/authors-list/', refs_views.AuthorsList.as_view(), name='authors-list'),
    path('references/genres-list/', refs_views.GenresList.as_view(), name='genres-list'),
    path('references/series-list/', refs_views.SeriesList.as_view(), name='series-list'),
    path('references/publishers-list/', refs_views.PublishersList.as_view(), name='publishers-list'),
    path('references/age_categories-list/', refs_views.AgeCategoriesList.as_view(), name='age_categories-list'),
    path('references/book_formats-list/', refs_views.BookFormatsList.as_view(), name='book_formats-list'),

    path('references/authors-delete/<int:pk>/', refs_views.AuthorsDelete.as_view(), name='authors-delete'),
    path('references/genres-delete/<int:pk>/', refs_views.GenresDelete.as_view(), name='genres-delete'),
    path('references/series-delete/<int:pk>/', refs_views.SeriesDelete.as_view(), name='series-delete'),
    path('references/publishers-delete/<int:pk>/', refs_views.PublishersDelete.as_view(), name='publishers-delete'),
    path('references/age_categories-delete/<int:pk>/', refs_views.AgeCategoriesDelete.as_view(), name='age_categories-delete'),
    path('references/book_formats-delete/<int:pk>/', refs_views.BookFormatsDelete.as_view(), name='book_formats-delete'),
    
    path('references/authors-update/<int:pk>/', refs_views.AuthorsUpdate.as_view(), name='authors-update'),
    path('references/genres-update/<int:pk>/', refs_views.GenresUpdate.as_view(), name='genres-update'),
    path('references/series-update/<int:pk>/', refs_views.SeriesUpdate.as_view(), name='series-update'),
    path('references/publishes-update/<int:pk>/', refs_views.PublishersUpdate.as_view(), name='publishers-update'),
    path('references/age_categories-update/<int:pk>/', refs_views.AgeCategoriesUpdate.as_view(), name='age_categories-update'),
    path('references/book_formats-update/<int:pk>/', refs_views.BookFormatsUpdate.as_view(), name='book_formats-update'),
    
    path('references/authors-create/', refs_views.AuthorsCreate.as_view(), name='authors-create'),
    path('references/genres-create/', refs_views.GenresCreate.as_view(), name='genres-create'),
    path('references/series-create/', refs_views.SeriesCreate.as_view(), name='series-create'),
    path('references/publishers-create/', refs_views.PublishersCreate.as_view(), name='publishers-create'),
    path('references/age_categories-create/', refs_views.AgeCategoriesCreate.as_view(), name='age_categories-create'),
    path('references/book_formats-create/', refs_views.BookFormatsCreate.as_view(), name='book_formats-create')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)