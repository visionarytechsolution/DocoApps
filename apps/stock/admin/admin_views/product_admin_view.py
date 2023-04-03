from django.contrib import admin
from apps.stock.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'brand', 'reference_number', 'barcode', 'purchase_price', 'selling_price', 'image', 'tenant', 'is_active', 'tax_category']
    list_display = ('name', 'brand', 'reference_number', 'barcode', 'purchase_price', 'selling_price', 'image', 'tenant', 'is_active', 'tax_category')
    search_fields = ('name', 'brand', 'reference_number', 'barcode', 'tenant__business_profile.name')
