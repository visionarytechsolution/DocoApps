from django.contrib import admin

from apps.common.models import MetricUnit


@admin.register(MetricUnit)
class MetricUnitAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'code', 'symbol']
    list_display = ('name', 'category', 'code', 'symbol')
    search_fields = ('name', 'category', 'code')
