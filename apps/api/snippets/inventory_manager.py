from apps.profile.models import *
from apps.stock.models import *
from rest_framework import serializers

def return_products(request):
    if DistributorProfile.objects.filter(admin_user_id=request.user.id).first() is not None:
        DBP = DistributorProfile.objects.filter(admin_user_id=request.user.id).first()
        Products = Product.objects.filter(tenant_id=DBP.tenant_id)
        print('Products')
        return Products
        
    elif EmployeeProfile.objects.filter(user_id=request.user.id).first() is not None:
        EMP = EmployeeProfile.objects.get(user_id=request.user.id)
        DBP = DistributorProfile.objects.filter(business_profile_id=EMP.employer_id).first()
        Products = Product.objects.filter(tenant_id=DBP.tenant_id)
        # Products = Order.objects.all()
        print('dd')

        return Products

def return_inventory(request):
    if DistributorProfile.objects.filter(admin_user_id=request.user.id).first() is not None:
        DBP = DistributorProfile.objects.filter(admin_user_id=request.user.id).first()
        iv = Inventory.objects.filter(tenant_id=DBP.tenant_id)

        return iv
        
    elif EmployeeProfile.objects.filter(user_id=request.user.id).first() is not None:
        EMP = EmployeeProfile.objects.get(user_id=request.user.id)
        DBP = DistributorProfile.objects.filter(business_profile_id=EMP.employer_id).first()
        iv = Inventory.objects.filter(tenant_id=DBP.tenant_id)

        return iv


