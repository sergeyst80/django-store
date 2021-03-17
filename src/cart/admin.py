from django.contrib import admin

# Register your models here.
from cart import models


class CustomerCartAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 
        'customer',
    ]


class BooksInCartAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 
        'customer_cart',
        'book_card',
        'qty',
        'price'
    ]


admin.site.register(models.CustomerCart, CustomerCartAdmin)
admin.site.register(models.BooksInCart, BooksInCartAdmin)