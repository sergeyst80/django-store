from django.contrib import admin


# Register your models here.
from orders import models


class OrderStatusesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.OrderStatuses._meta.fields]


class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.CustomerOrder._meta.fields]


admin.site.register(models.OrderStatuses, OrderStatusesAdmin)
admin.site.register(models.CustomerOrder, CustomerOrderAdmin)
