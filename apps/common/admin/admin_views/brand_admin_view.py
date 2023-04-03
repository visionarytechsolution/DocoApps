from django.contrib import admin

from apps.common.models.brand import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    fields = ['name', 'code', 'logo']
    list_display = ('name', 'code', 'logo')
    search_fields = ('name', 'code')
