from django.contrib import admin
from apps.common.models import Address


class AddressInline(admin.StackedInline):
    model = Address
    can_delete = True
    verbose_name_plural = 'addresses'
