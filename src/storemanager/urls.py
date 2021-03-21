from django.urls import path
from storemanager import views


app_name = 'storemanager'

urlpatterns = [
    path('create-bookcard/', views.CreateBookCardView.as_view(), name='create-bookcard'),
    path('update-bookcard/<int:pk>/', views.UpdateBookCardView.as_view(), name='update-bookcard'),
    path('detail-bookcard/<int:pk>/', views.DetailBookCardView.as_view(), name='detail-bookcard'),
    path('list-bookcards/', views.ListBookCardsView.as_view(), name='list-bookcards')
]