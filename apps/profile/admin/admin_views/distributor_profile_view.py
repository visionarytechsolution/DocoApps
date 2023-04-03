from django.contrib import admin

from apps.profile.models import DistributorProfile


@admin.register(DistributorProfile)
class DistributorProfileAdmin(admin.ModelAdmin):
    fields = ['business_profile', 'admin_user', 'code']
    list_display = ('business_profile', 'admin_user', 'code')
    search_fields = ('business_profile', 'admin_user', 'code')
