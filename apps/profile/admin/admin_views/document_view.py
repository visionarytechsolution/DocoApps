from django.contrib import admin

from apps.profile.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    fields = ['type', 'file', 'identification_number', 'expiry_date', 'notes']
    list_display = ('type', 'file', 'identification_number', 'expiry_date', 'notes')
    search_fields = ('type', 'identification_number')
