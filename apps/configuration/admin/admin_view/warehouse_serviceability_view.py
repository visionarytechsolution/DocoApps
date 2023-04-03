from django.contrib import admin
from apps.configuration.models.warehouse_serviceability import WarehouseServiceability


@admin.register(WarehouseServiceability)
class WarehouseServiceabilityAdmin(admin.ModelAdmin):
    fields = ['warehouse', 'area']
    list_display = ('warehouse', 'area', 'created_at')
    search_fields = ('warehouse',)
