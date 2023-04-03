from django.contrib import admin
from apps.configuration.models.offer import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    fields = ['tenant', 'applied_on', 'deduction_type', 'applicable_from', 'expire_after', 'value']
    list_display = ('tenant', 'applied_on', 'deduction_type', 'applicable_from', 'expire_after', 'value', 'created_at')
    search_fields = ('tenant', 'applied_on', 'deduction_type')
