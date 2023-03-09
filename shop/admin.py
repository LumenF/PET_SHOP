from django.contrib import admin

from shop.models import OrderModel, ContactModel


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'address',
    )


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'value',
    )
