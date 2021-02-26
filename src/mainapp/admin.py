from django.contrib import admin

# Register your models here.
from mainapp import models as mainapp_models


class MainAppAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 
        'name',
        'picture',
        'cost',
        'get_authors',
        'series',
        'get_genres',
        'year',
        'num_pages',
        'book_format',
        'isbn',
        'weight',
        'age_category',
        'publisher',
        'qty',
        'is_active',
        'rating',
        'create_date',
        'update_date'
    ]

admin.site.register(mainapp_models.BookCard, MainAppAdmin)
