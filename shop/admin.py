from django.contrib import admin

from shop.models import OrderModel


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'address',
    )
