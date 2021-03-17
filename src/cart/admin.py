from django.contrib import admin

# Register your models here.
from cart import models


class CustomerCartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.CustomerCart._meta.fields]


class BooksInCartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.BooksInCart._meta.fields]


admin.site.register(models.CustomerCart, CustomerCartAdmin)
admin.site.register(models.BooksInCart, BooksInCartAdmin)
