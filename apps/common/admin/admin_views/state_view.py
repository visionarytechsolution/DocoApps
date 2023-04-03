from django.contrib import admin

from apps.common.models import State


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    fields = ['name', 'code']
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
