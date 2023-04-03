from django.contrib import admin

from apps.profile.models import RetailerProfile


@admin.register(RetailerProfile)
class RetailerProfileAdmin(admin.ModelAdmin):
    fields = ['business_profile', 'admin_user']
    list_display = ('business_profile', 'admin_user')
    search_fields = ('business_profile', 'admin_user')
