from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bangazonapi.views.customer_view import CustomerView
from bangazonapi.views.product_view import ProductView
from bangazonapi.views.order_view import OrderView
from bangazonapi.views.orderproduct_view import OrderProductView
from bangazonapi.views.auth import register_user, check_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerView, 'customer')
router.register(r'orders', OrderView, 'order')
router.register(r'products', ProductView, 'product')
router.register(r'order_products', OrderProductView, 'order_products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/orders/<int:pk>/add_to_cart/', OrderView.as_view({'post': 'add_to_cart'}), name='add_to_cart'),
    path('api/orders/<int:pk>/remove_from_cart/<int:product_id>/', OrderView.as_view({'delete': 'remove_from_cart'}), name='remove_from_cart'),
    path('register', register_user),
    path('checkuser', check_user),
]
