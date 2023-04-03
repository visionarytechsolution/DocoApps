from django.contrib import admin

from apps.profile.models import DocoUser


class DocoUserInline(admin.StackedInline):
    model = DocoUser
    can_delete = False
    verbose_name_plural = 'doco users'
