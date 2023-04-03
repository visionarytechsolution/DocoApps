from django.contrib import admin
from apps.configuration.models.warehouse import Warehouse
from apps.profile.models import DistributorProfile
from apps.profile.models.doco_user import DocoUserType


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    fields = ['distributor', 'address']
    list_display = ('distributor', 'address', 'created_at')
    search_fields = ('distributor',)

    def save_model(self, request, obj, form, change):
        if request.user.type == DocoUserType.DISTRIBUTOR:
            tenant = DistributorProfile.objects.get_distributor_for_admin_user(request.user)
            obj.tenant = tenant
        if request.user.type == DocoUserType.DOCO_ADMIN:
            obj.tenant = obj.distributor
        super().save_model(request, obj, form, change)
