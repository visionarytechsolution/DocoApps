from django.contrib import admin

from apps.sells.models import OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    fields = ['order', 'product', 'quantity', 'unit', 'tenant', 'is_active']
    list_display = ('order', 'product', 'quantity', 'unit', 'tenant', 'is_active')
    search_fields = ('order__order_id', 'product__name')
