from django.urls import path
from . import views


app_name = 'references'

urlpatterns = [
    path('authors-list/', views.AuthorsList.as_view(), name='authors-list'),
    path('genres-list/', views.GenresList.as_view(), name='genres-list'),
    path('series-list/', views.SeriesList.as_view(), name='series-list'),
    path('publishers-list/', views.PublishersList.as_view(), name='publishers-list'),
    path('age_categories-list/', views.AgeCategoriesList.as_view(), name='age_categories-list'),
    path('book_formats-list/', views.BookFormatsList.as_view(), name='book_formats-list'),

    path('authors-delete/<int:pk>/', views.AuthorsDelete.as_view(), name='authors-delete'),
    path('genres-delete/<int:pk>/', views.GenresDelete.as_view(), name='genres-delete'),
    path('series-delete/<int:pk>/', views.SeriesDelete.as_view(), name='series-delete'),
    path('publishers-delete/<int:pk>/', views.PublishersDelete.as_view(), name='publishers-delete'),
    path('age_categories-delete/<int:pk>/', views.AgeCategoriesDelete.as_view(), name='age_categories-delete'),
    path('book_formats-delete/<int:pk>/', views.BookFormatsDelete.as_view(), name='book_formats-delete'),
    
    path('authors-update/<int:pk>/', views.AuthorsUpdate.as_view(), name='authors-update'),
    path('genres-update/<int:pk>/', views.GenresUpdate.as_view(), name='genres-update'),
    path('series-update/<int:pk>/', views.SeriesUpdate.as_view(), name='series-update'),
    path('publishes-update/<int:pk>/', views.PublishersUpdate.as_view(), name='publishers-update'),
    path('age_categories-update/<int:pk>/', views.AgeCategoriesUpdate.as_view(), name='age_categories-update'),
    path('book_formats-update/<int:pk>/', views.BookFormatsUpdate.as_view(), name='book_formats-update'),
    
    path('authors-create/', views.AuthorsCreate.as_view(), name='authors-create'),
    path('genres-create/', views.GenresCreate.as_view(), name='genres-create'),
    path('series-create/', views.SeriesCreate.as_view(), name='series-create'),
    path('publishers-create/', views.PublishersCreate.as_view(), name='publishers-create'),
    path('age_categories-create/', views.AgeCategoriesCreate.as_view(), name='age_categories-create'),
    path('book_formats-create/', views.BookFormatsCreate.as_view(), name='book_formats-create')
]
