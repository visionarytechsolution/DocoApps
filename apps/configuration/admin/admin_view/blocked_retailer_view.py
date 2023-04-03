from django.contrib import admin
from apps.configuration.models.blocked_retailer import BlockedRetailer


@admin.register(BlockedRetailer)
class BlockedRetailerAdmin(admin.ModelAdmin):
    fields = ['retailer', 'distributor', 'reason']
    list_display = ('retailer', 'distributor', 'reason', 'created_at')
    search_fields = ('retailer', 'distributor', 'reason')
