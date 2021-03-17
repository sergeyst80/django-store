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
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static


from mainapp import views as main_views
from references import urls as refs_urls
from users import urls as users_urls
from cart import urls as cart_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.HomePage.as_view(), name='homepage'),
    path('books-catalog', main_views.BooksCatalog.as_view(), name='books-catalog'),
    path('references/', include(refs_urls, namespace='references')),
    path('users/', include(users_urls, namespace='users')),
    path('cart/', include(cart_urls, namespace='cart')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)