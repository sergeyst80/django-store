from django.contrib import admin

# Register your models here.
from .models import Authors, Countries, Genres, Publishers, Series


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name', 'country', 'date_of_birth']

class CountriesGenresSeriesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

class PublishersAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'country']

admin.site.register(Countries, CountriesGenresSeriesAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Series, CountriesGenresSeriesAdmin)
admin.site.register(Genres, CountriesGenresSeriesAdmin)
admin.site.register(Publishers, PublishersAdmin)