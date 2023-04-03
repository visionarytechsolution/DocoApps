from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm

from apps.profile.models import DocoUser
from django.contrib import admin


class DocoUserCreationForm(UserCreationForm):
    class Meta:
        model = DocoUser
        fields = '__all__'


@admin.register(DocoUser)
class DocoUserAdmin(BaseUserAdmin):
    model = DocoUser
    add_form = DocoUserCreationForm
    list_display = ("username", 'first_name', 'last_name', "email", 'date_joined', 'type')
    search_fields = ("username", "email", 'type')


fields = list(BaseUserAdmin.fieldsets)
fields[1] = ("Profile", {'fields': ("first_name", "last_name", "email", 'type')})
BaseUserAdmin.fieldsets = tuple(fields)
