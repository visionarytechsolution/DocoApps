from django.urls import include
from django.urls import path

from apps.api import views

urlpatterns = [
    path('v1/', include(('apps.api.v1.urls', 'api'), namespace='v1')),

    path('orders/', views.Orders, name="orders"),
    path('order/<str:pk>/', views.Order_s, name="order_s"),
    path('retailers/', views.retailer_list, name="retailer_list"),
    path('retailers-search/<int:page>/', views.retailers_search, name="retailers_search"), # DONE
    path('products/', views.product_list, name="product_list"),
    path('product/<str:pk>/', views.product_single, name="product_single"),
    path('inventory/', views.inventory_list, name="inventory_list"),
    # path('offer/', views.Inventory, name="retailers"),
    # path('bde/', views.Bde, name="bde"),
]
