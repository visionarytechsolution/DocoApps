from django.contrib import admin

from apps.profile.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fields = ['address_line1', 'address_line2', 'is_verified', 'area', 'latitude', 'longitude']
    list_display = ('address_line1', 'is_verified', 'area', 'latitude', 'longitude')
    search_fields = ('address_line1', 'area__zip_code', 'area__name')
