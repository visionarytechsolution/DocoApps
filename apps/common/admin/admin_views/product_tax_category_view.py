from django.contrib import admin

from apps.common.models import ProductTaxCategory


@admin.register(ProductTaxCategory)
class ProductTaxCategoryAdmin(admin.ModelAdmin):
    fields = ['category', 'state', 'gst', 'sgst', 'igst']
    list_display = ('category', 'state', 'gst', 'sgst', 'igst')
    search_fields = ('category', 'state',)
