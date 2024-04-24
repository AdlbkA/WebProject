from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Product, CartItem, Cart
from .serializers import CategorySerializer, ProductSerializer, UserSerializer, CartSerializer, CartItemSerializer


@api_view(["GET"])
@csrf_exempt
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
def category_detail(request, pk=None):
    try:
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})


@csrf_exempt
@api_view(['GET'])
def category_products_by_id(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category_id=id)
    data = {'products': list(products.values())}
    return JsonResponse(data)


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserSignUpAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message": "User created successfully", "user_id": user.id}, status=status.HTTP_201_CREATED)


class CartView(APIView):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class AddCartItemView(APIView):
    def post(self, request, product_id):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product, pk=product_id)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += 1
            item.save()
        serializer = CartItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateCartItemView(APIView):
    def put(self, request, item_id):
        item = get_object_or_404(CartItem, id=item_id)
        item.quantity = request.data.get('quantity', item.quantity)
        item.save()
        return Response({"message": "Cart item updated successfully"}, status=status.HTTP_200_OK)


class DeleteCartItemView(APIView):
    def delete(self, request, item_id):
        item = get_object_or_404(CartItem, id=item_id)
        item.delete()
        return Response({"message": "Cart item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
