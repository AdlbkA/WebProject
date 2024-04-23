from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=None)
    price = serializers.FloatField()
    image = serializers.CharField(max_length=None)
    quantity = serializers.IntegerField()
    rating = serializers.FloatField()
    category_id = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'quantity', 'rating', 'category_id')


class SupplierSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    rating = serializers.FloatField()
    product = ProductSerializer()

    def create(self, validated_data):
        instance = Supplier.objects.create(
            name=validated_data.get('name'),
            rating=validated_data.get('rating'),
            product=validated_data.get('product')
        )

        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.rating = validated_data.get('rating', instance.name)
        instance.product = validated_data.get('product', instance.product)

        instance.save()

        return instance

    def delete(self, instance):
        instance.delete()


class DeliverySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    rating = serializers.FloatField()
    product = ProductSerializer()

    def create(self, validated_data):
        instance = Supplier.objects.create(
            name=validated_data.get('name'),
            rating=validated_data.get('rating'),
            product=validated_data.get('product')
        )

        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.rating = validated_data.get('rating', instance.name)
        instance.product = validated_data.get('product', instance.product)

        instance.save()

        return instance

    def delete(self, instance):
        instance.delete()
