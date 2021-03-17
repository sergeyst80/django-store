from django.contrib import admin

# Register your models here.
from users import models


class ExtUserDataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.ExtUserData._meta.fields]


admin.site.register(models.ExtUserData, ExtUserDataAdmin)
