from django.contrib import admin
from apps.configuration.models.product_offer import ProductOffer


@admin.register(ProductOffer)
class ProductOfferAdmin(admin.ModelAdmin):
    fields = ['tenant', 'product', 'offer']
    list_display = ('tenant', 'product', 'offer', 'created_at')
    search_fields = ('product', 'offer')
