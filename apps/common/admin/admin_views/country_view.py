from django.contrib import admin

from apps.common.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ['name', 'code', 'alpha_three_code', 'currency_code']
    list_display = ('name', 'code', 'alpha_three_code', 'currency_code')
    search_fields = ('name', 'code', 'alpha_three_code', 'currency_code')
