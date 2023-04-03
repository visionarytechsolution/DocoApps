from django.contrib import admin

from apps.sells.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ['created_by', 'buyer', 'is_approved', 'order_value', 'status', 'tenant', 'is_active']
    list_display = ('created_by', 'order_id', 'buyer', 'is_approved', 'order_value', 'status', 'tenant', 'is_active')
    search_fields = ('created_by', 'order_id', 'buyer', 'status')