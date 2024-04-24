from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', category_list),
    path('products/', products_method),
    path('supliers/', SupplierList.as_view()),
    path('deliverers/', DeliveryList.as_view()),
    path('products/<int:id>', update_product)
]