from django.contrib import admin

# Register your models here.
from mainapp import models


class BookCardAdmin(admin.ModelAdmin):
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

class BookCommentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.BookComments._meta.fields]

admin.site.register(models.BookCard, BookCardAdmin)
admin.site.register(models.BookComments, BookCommentsAdmin)
