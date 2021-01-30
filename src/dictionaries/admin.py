from django.contrib import admin

# Register your models here.
from .models import Authors, Countries, Genres, Publishers, Series

admin.site.register(Countries)
admin.site.register(Authors)
admin.site.register(Series)
admin.site.register(Genres)
admin.site.register(Publishers)