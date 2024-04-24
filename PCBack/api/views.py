from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product, Supplier, Delivery
from .serializers import CategorySerializer, ProductSerializer, SupplierSerializer, DeliverySerializer


@api_view(["GET"])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def products_method(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == "POST" and not request.path.endswith('/'):
        return redirect(request.get_full_path() + '/v')
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == "PUT":
    #     try:
    #         product = Product.objects.get(id=id)
    #     except Product.DoesNotExist as e:
    #         return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    #     serializer = ProductSerializer(product, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == "DELETE":
    #     try:
    #         product = Product.objects.get(id=id)
    #     except Product.DoesNotExist as e:
    #         return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    #     product.delete()
    #     return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# @api_view(["POST"])
# def create_product(request):
#     if request.method == 'POST' and not request.path.endswith('/'):
#         return redirect(request.get_full_path() + '/')
#     if request.method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "DELETE"])
def update_product(request, id=None):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# @api_view(["DELETE"])
# def delete_product(request, id=None):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist as e:
#         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == "DELETE":
#         product.delete()
#         return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class SupplierList(APIView):
    def get(self, request):
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)


class DeliveryList(APIView):
    def get(self, request):
        deliveries = Delivery.objects.all()
        serializer = DeliverySerializer(deliveries, many=True)
        return Response(serializer.data)
