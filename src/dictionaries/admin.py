from django.contrib import admin

# Register your models here.
from . import models


class DictionariesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


admin.site.register(models.Authors, DictionariesAdmin)
admin.site.register(models.Series, DictionariesAdmin)
admin.site.register(models.Genres, DictionariesAdmin)
admin.site.register(models.Publishers, DictionariesAdmin)