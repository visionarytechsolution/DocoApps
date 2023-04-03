from django.contrib import admin
from apps.stock.models import ProductUnitConversion


@admin.register(ProductUnitConversion)
class ProductUnitConversionAdmin(admin.ModelAdmin):
    fields = ['from_unit', 'to_unit', 'factor', 'tenant', 'is_active']
    list_display = ('from_unit', 'to_unit', 'factor', 'tenant', 'is_active')
    search_fields = ('from_unit', 'to_unit')


