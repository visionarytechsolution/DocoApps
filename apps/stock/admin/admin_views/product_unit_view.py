from django.contrib import admin
from apps.stock.models import ProductUnit


@admin.register(ProductUnit)
class ProductUnitAdmin(admin.ModelAdmin):
    fields = ['product', 'unit', 'is_default', 'tenant', 'is_active']
    list_display = ('product', 'unit', 'is_default', 'tenant', 'is_active')
    search_fields = ('product', 'unit', 'tenant',)
