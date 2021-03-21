from django.contrib import admin

# Register your models here.
from mainapp import models


class BookCardAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.BookCard._meta.fields]


class BookCommentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.BookComments._meta.fields]

admin.site.register(models.BookCard, BookCardAdmin)
admin.site.register(models.BookComments, BookCommentsAdmin)
