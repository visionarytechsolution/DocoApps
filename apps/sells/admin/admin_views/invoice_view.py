from django.contrib import admin

from apps.sells.models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    fields = ['order', 'due_date', 'invoice_value', 'tenant', 'is_active']
    list_display = ('order', 'invoice_id', 'due_date', 'invoice_value', 'tenant', 'is_active')
    search_fields = ('order__order_id', 'invoice_id')
