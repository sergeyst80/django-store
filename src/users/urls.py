from django.urls import path
from django.contrib.auth import views as auth_views
from users import views


app_name = 'users'

urlpatterns = [
    path('create-user/', views.UserCreationView.as_view(), name='create-user'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('update-user/', views.UserUpdateView.as_view(), name='update-user'),
    path('logout/', views.UserLogoutView.as_view(), name='logout')
]