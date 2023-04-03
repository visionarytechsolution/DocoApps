from django.contrib import admin

from apps.common.models import PackageDimension


@admin.register(PackageDimension)
class PackageDimensionAdmin(admin.ModelAdmin):
    fields = ['dimension_unit', 'length', 'width', 'height', 'weight_unit', 'weight']
    list_display = ('dimension_unit', 'length', 'width', 'height', 'weight_unit', 'weight')
    search_fields = ('dimension_unit', 'weight_unit')
