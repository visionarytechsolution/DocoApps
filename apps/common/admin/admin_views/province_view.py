from django.contrib import admin

from apps.common.models import Province


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    fields = ['name', 'code', 'country', 'state']
    list_display = ('name', 'code', 'country', 'state')
    search_fields = ('name', 'code')
