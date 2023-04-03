from django.contrib import admin

from apps.profile.models import BusinessProfile


@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    fields = ['name', 'type', 'contact_person_name', 'contact_person_designation', 'phone_number', 'email', 'number_verified']
    list_display = ('name', 'type', 'contact_person_name', 'phone_number', 'email')
    search_fields = ('name', 'phone_number', 'contact_person_name')
