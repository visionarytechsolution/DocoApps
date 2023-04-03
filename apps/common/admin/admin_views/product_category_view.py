from django.contrib import admin

from apps.common.models.product_category import ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'code']
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

