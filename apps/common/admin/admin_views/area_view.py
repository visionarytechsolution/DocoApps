from django.contrib import admin

from apps.common.models import Area


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    fields = ['name', 'code', 'zip_code', 'province']
    list_display = ('name', 'code', 'zip_code', 'province')
    search_fields = ('name', 'code', 'zip_code', 'province')
