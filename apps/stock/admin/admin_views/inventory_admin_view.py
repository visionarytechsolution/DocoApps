from django.contrib import admin
from apps.stock.models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    fields = ['product', 'current_stock', 'minimum_stock', 'stock_unit', 'tenant', 'is_active']
    list_display = ('product', 'current_stock', 'minimum_stock', 'stock_unit', 'tenant', 'is_active')
    search_fields = ('product', 'tenant__business_profile.name')
