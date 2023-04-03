from django.contrib import admin

from apps.common.models import IdentificationDocument


@admin.register(IdentificationDocument)
class IdentificationDocumentAdmin(admin.ModelAdmin):
    fields = ['document_type', 'front', 'back', 'identification_number', 'expiry_date', 'notes']
    list_display = ('identification_number', 'document_type', 'front', 'back', 'expiry_date')
    search_fields = ('identification_number',)
