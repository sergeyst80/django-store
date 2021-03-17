from django.contrib import admin

# Register your models here.
from mainapp import models


class MainAppAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.BookCard._meta.fields]

admin.site.register(models.BookCard, MainAppAdmin)
