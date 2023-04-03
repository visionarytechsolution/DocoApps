from django.contrib import admin

from apps.profile.models.employee_profile import EmployeeProfile


@admin.register(EmployeeProfile)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['user', 'employee_code', 'joining_date', 'primary_number', 'whatsapp_number', 'number_verified',
              'email_verified', 'address', 'employer', 'id_proof', 'address_proof']
    list_display = ('user', 'employee_code', 'primary_number', 'whatsapp_number', 'employer')
    search_fields = ('user', 'employee_code', 'primary_number', 'whatsapp_number', 'employer__name')
