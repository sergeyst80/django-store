from django.contrib import admin

# Register your models here.
from users import models


class ExtUserDataAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'phone', 'country', 'city', 'post_index', 'address1' ,'address2']


admin.site.register(models.ExtUserData, ExtUserDataAdmin)
