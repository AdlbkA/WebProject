from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import *

urlpatterns = [
    path('categories/', category_list, name='category-list'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),
    path('categories/<int:id>/products/', category_products_by_id, name='category-products'),

    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', AddCartItemView.as_view(), name='add-cart-item'),
    path('cart/update/<int:item_id>/', UpdateCartItemView.as_view(), name='update-cart-item'),
    path('cart/delete/<int:item_id>/', DeleteCartItemView.as_view(), name='delete-cart-item'),

    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),

    path('signup/', UserSignUpAPIView.as_view(), name='user-signup'),
    path('sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('sign-in/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]