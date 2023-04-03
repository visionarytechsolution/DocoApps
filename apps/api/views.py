from django.http import JsonResponse
from .snippets.serializers import *
from django.views.decorators.csrf import csrf_exempt
from apps.sells.models import *
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .snippets.return_orders import return_orders
from .snippets.inventory_manager import *
from apps.profile.models import *
from rest_framework import status
from django.core.paginator import Paginator

# Register
def register(request):
    pass

@csrf_exempt
@api_view(['GET', 'POST'])
def Orders(request):
    if request.method == 'GET':
        serializers = OrderSerializer(return_orders(request), many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        print(request.data)
        serializers = OrderSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Order_s(request, pk):
    if request.method == 'GET':
        o = Order.objects.filter(order_id=pk).first()
        serializers = OrderSerializer(o)
        return Response(serializers.data)
    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        print(request.data)
        serializers = OrderSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)


@csrf_exempt
@api_view(['GET', 'POST'])
def retailer_list(request):
    if request.method == 'GET':
        # BDE searching for retailers in his area
        print(request.user.type)
        if request.user.type == 'DISTRIBUTOR':
            DP = DistributorProfile.objects.filter(admin_user_id=request.user.id).first()
            # EMP_BP = BusinessProfile.objects.filter(id=DP.business_profile_id).first()
            EMP_BP = BusinessProfile.objects.filter(id=DP.business_profile.id).first()
        if request.user.type == 'UNSPECIFIED':
            EMP = EmployeeProfile.objects.filter(user_id=request.user.id).first()
            DP = DistributorProfile.objects.filter(id=EMP.employer_id).first()
            EMP_BP = BusinessProfile.objects.filter(id=DP.business_profile_id).first()
        retailers = RetailerProfile.objects.filter(business_profile__address__area__zip_code=EMP_BP.address.area.zip_code)
        if retailers:
            serializers = RetailerProfileSerializer(retailers, many=True)
            return JsonResponse(serializers.data, safe=False)
        else:
            return JsonResponse({'not_found':'No retailers found where your business server!'}, status=404)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = RetailerProfileSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=201)
        return JsonResponse(serializers.errors, status=400)


@csrf_exempt
@api_view(['GET'])
def retailers_search(request, page):
    if request.method == 'GET':
        EMP_BP = None
        if request.user.type == 'DISTRIBUTOR':
            DP = DistributorProfile.objects.filter(admin_user_id=request.user.id).first()
            # EMP_BP = BusinessProfile.objects.filter(id=DP.business_profile_id).first()
            EMP_BP = BusinessProfile.objects.filter(id=DP.business_profile.id).first()
        if request.user.type == 'UNSPECIFIED':
            EMP = EmployeeProfile.objects.filter(user_id=request.user.id).first()
            DP = DistributorProfile.objects.filter(id=EMP.employer_id).first()
            EMP_BP = BusinessProfile.objects.filter(id=DP.business_profile_id).first()
        # contains = request.GET.get('contains', False)
        # contains = request.GET.get('contains', False)
        # contains = request.GET.get('contains', False)
        try:
            contains = request.GET['contains']
            retailers = RetailerProfile.objects.filter(business_profile__address__area__zip_code=EMP_BP.address.area.zip_code, business_profile__name__contains = contains)
        except:
            retailers = RetailerProfile.objects.filter(business_profile__address__area__zip_code=EMP_BP.address.area.zip_code)

        page_paginate = page_count(retailers)
        retailers = retailers[paginate(page)[0]:paginate(page)[1]]
        op_retailers = []
        for r in retailers:
            r_dict = {}
            r_dict['id'] = r.id
            r_dict['name'] = r.business_profile.name
            # r_dict['bus_profile_picture'] = r.business_profile.name
            # Search in Order table where DP and RP are the foreignkeys
            orders = Order.objects.filter(buyer=r, tenant_id=DP.tenant_id)
            total_payment = ''
            for o in orders:
                iv = Invoice.objects.filter(order=o).first()
                if iv:
                    total_payment += iv
            r_dict['total_orders'] = orders.count()
            r_dict['total_payment'] = total_payment
            op_retailers.append(r_dict)
        op_retailers.append({'page_count':page_paginate})
        if retailers:
            serializers = RetailerProfileSerializer(retailers, many=True)
            return JsonResponse(op_retailers, safe=False)
        else:
            return JsonResponse({'not_found':'No retailers found!'}, status=404)




@csrf_exempt
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        serializers = ProductSerializer(return_products(request), many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

@csrf_exempt
@api_view(['GET', 'POST'])
def inventory_list(request):
    if request.method == 'GET':
        serializers = InventorySerializer(return_inventory(request), many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def product_single(request, pk):
    try:
        product = Product.objects.get(reference_number=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = ProductSerializer(product, many=True)
        return Response(serializers.data)
    if request.method == 'PUT':
        serializers = ProductSerializer(product, data=request.data, many=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def Offer(request):
#     if request.method == 'GET':
#         serializers = ProductOfferSerializer(return_products(request), many=True)
#         return Response(serializers.data)
#     elif request.method == 'POST':
#         # data = JSONParser().parse(request)
#         print(request.data)
#         serializers = ProductOfferSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=201)
#         return Response(serializers.errors, status=400)

