from apps.profile.models import *

from apps.sells.models import Order

def return_orders(request):
    if DistributorProfile.objects.filter(admin_user_id=request.user.id).first() is not None:
        DBP = DistributorProfile.objects.filter(admin_user_id=request.user.id).first()
        orders = Order.objects.filter(tenant_id=DBP.tenant_id)
        print('orders')
        return orders
        
    elif EmployeeProfile.objects.filter(user_id=request.user.id).first() is not None:
        EMP = EmployeeProfile.objects.get(user_id=request.user.id)
        DBP = DistributorProfile.objects.filter(business_profile_id=EMP.employer_id).first()
        orders = Order.objects.filter(tenant_id=DBP.tenant_id)
        # orders = Order.objects.all()
        print('dd')

        return orders


    elif RetailerProfile.objects.filter(admin_user_id=request.user.id).first() is not None:
        print("Is RetailerProfile")
    

def filter_retailers_by_zip(request):
    if DistributorProfile.objects.filter(admin_user_id=request.user.id).first() is not None:
        print("Is Distributor")
        
    elif EmployeeProfile.objects.filter(user_id=request.user.id).first() is not None:
        EMP = EmployeeProfile.objects.get(user_id=request.user.id)
        EMP_BP = BusinessProfile.objects.filter(id=EMP.employer_id).first()
        retailers = RetailerProfile.objects.filter(businessprofile__id=EMP.employer_id)
        retailers = RetailerProfile.objects.filter()
        # orders = Order.objects.all()

        return retailers


    elif RetailerProfile.objects.filter(admin_user_id=request.user.id).first() is not None:
        print("Is RetailerProfile")
