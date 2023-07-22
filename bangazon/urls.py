from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bangazonapi.views.customer_view import CustomerView
from bangazonapi.views.seller_view import SellerView
from bangazonapi.views.product_view import ProductView
from bangazonapi.views.order_view import OrderView
from bangazonapi.views.auth import register_user, check_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerView, 'customer')
router.register(r'orders', OrderView, 'order')
router.register(r'products', ProductView, 'product')
router.register(r'sellers', SellerView, 'seller')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
