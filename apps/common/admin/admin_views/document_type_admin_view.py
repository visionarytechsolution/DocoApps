from django.contrib import admin

from apps.common.models import DocumentType


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'has_unique_number', 'has_back_image', 'has_expiry_date']
    list_display = ('name', 'has_unique_number', 'has_back_image', 'has_expiry_date')
    search_fields = ('name',)
