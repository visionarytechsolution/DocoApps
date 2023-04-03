from rest_framework import serializers
from apps.profile.models import *
from apps.sells.models import Order, OrderItem
from apps.stock.models import *
from apps.configuration.models import ProductOffer
from rest_framework import permissions
from apps.common.models import *
from apps.common.models.brand import Brand
from django.contrib.auth.models import Group
from .snip import *
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # fields = ['id', 'created_by', 'order_id', 'buyer', 'is_approved', 'approved_by', 'approved_at',
        #         'comment', 'status', 'order_value']
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        # fields = ('id','name','code','zip_code','province','latitude','longitude',)
        fields = '__all__'


class ProvenceSerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = Province
        # fields = ('id','name','code','zip_code','province','latitude','longitude',)
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):
    province = ProvenceSerializer()

    class Meta:
        model = Area
        fields = ('id', 'name', 'code', 'zip_code', 'province',)


class AddressSerializer(serializers.ModelSerializer):
    area = AreaSerializer()

    class Meta:
        model = Address
        fields = ('id', 'area', 'address_line1', 'address_line2', 'is_verified', 'latitude', 'longitude',)


class BusinessProfileProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = BusinessProfile
        fields = ('name', 'address', 'contact_person_name', 'contact_person_designation', 'phone_number', 'email',)


class DocoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocoUser
        fields = ('id', 'last_login', 'username', 'first_name', 'email', 'is_active', 'date_joined', 'type',)


class DistributorProfileSerializer(serializers.ModelSerializer):
    business_profile = BusinessProfileProfileSerializer()
    admin_user = DocoUserSerializer()

    class Meta:
        model = DistributorProfile
        fields = ('id', 'created_at', 'tenant_id', 'admin_user', 'business_profile',)


class RetailerProfileSerializer(serializers.ModelSerializer):
    business_profile = BusinessProfileProfileSerializer()
    admin_user = DocoUserSerializer()

    class Meta:
        model = RetailerProfile
        # fields = ['id', 'created_by', 'order_id', 'buyer', 'is_approved', 'approved_by', 'approved_at',
        #         'comment', 'status', 'order_value', 'tenant']   
        fields = '__all__'

    def create(self, validated_data):
        du = validated_data.pop('admin_user')
        user = DocoUser.objects.create(**du)
        if user:                
            bp = validated_data.pop('business_profile')
            area = bp.pop('address').pop('area')
            area = Area.objects.filter(zip_code=area.pop('zip_code')).first()
            adr = Address.objects.filter(area=area).first()
            business_profile = BusinessProfile.objects.create(address=adr, **bp)
            if business_profile:
                RP = RetailerProfile.objects.create(admin_user=user, business_profile=business_profile)
                RP.set_password(random_password())
                RP.save()
                # phone = validated_data.pop('phone_number')
                # email_or_sms_it()
                if RP:
                    groups = Group.objects.get(name='RETAILER') 
                    groups.user_set.add(user)
                    return RP
                else:
                    business_profile.delete()
                    user.delete()
                    return 0
            else:
                user.delete()
            return 0
        else:
            return 0

class RetailerProfileforOrderPunchingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DistributorProfile()
        fields = ('tenant_id','code',)

    # def return_order_count(self, data):
    #     Order.objects.filter(buyer__=)


# Send back all products
# Send back all products
# Send back all products
# Send back all products
class tenant(serializers.ModelSerializer):
    
    class Meta:
        model = DistributorProfile()
        fields = ('tenant_id','code',)

class ProductSerializer(serializers.ModelSerializer):
    custom_field = serializers.SerializerMethodField()

    def get_custom_field(self, obj):
        x = 10
        return x
    class Meta:
        model = Product
        fields = ("__all__")

class ProductOfferSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductOffer
        fields = ("__all__")

# BDE APP 
# BDE APP 
# BDE APP 
# BDE APP 
# 
# Page: PRODUCT / SKUs
class BDE_BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("name","code","logo",)

class BDE_ProductSerializer(serializers.ModelSerializer):
    brand = BDE_BrandSerializer()
    offers = serializers.SerializerMethodField()

    def get_offers(self, obj):
        offers = ProductOffer.objects.filter(product__reference_number=obj.reference_number)
        return offers
    
    class Meta:
        model = Product
        fields = ("name","image","reference_number","selling_price","purchase_price","brand","offers",)

class BDE_MetricUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetricUnit
        fields = ("name","code","symbol",)

class BDE_ProductUnitSerializer(serializers.ModelSerializer):
    unit = BDE_MetricUnitSerializer()
    class Meta:
        model = ProductUnit
        # fields = ("is_active","is_default")
        fields = ("unit",)

class InventorySerializer(serializers.ModelSerializer):
    product = BDE_ProductSerializer()
    stock_unit = BDE_ProductUnitSerializer()
    class Meta:
        model = Inventory
        fields = ("product","current_stock", "stock_unit")