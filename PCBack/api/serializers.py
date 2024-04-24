from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#
#     class Meta:
#         model = Category
#         fields = ['id', 'name']
#
#
# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     name = serializers.CharField()
#     surname = serializers.CharField()
#     password = serializers.CharField()
#
#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         user = User.objects.create(**validated_data)
#         return user
#
#
# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField(max_length=255)
#     price = serializers.FloatField()
#     image = serializers.CharField(max_length=255)
#     quantity = serializers.IntegerField()
#     rating = serializers.FloatField()
#     category_id = serializers.IntegerField(read_only=True)
#
#     def create(self, validated_data):
#         category_id = Category.objects.get(pk=validated_data['category_id'])
#         return Product.objects.create(category_id=category_id, **validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.image = validated_data.get('image', instance.image)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.rating = validated_data.get('rating', instance.quantity)
#         instance.category_id = validated_data.get('category_id', instance.category_id)
#
#         instance.save()
#
#         return instance
#
#
# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = ['id', 'product', 'quantity']
#
#
# class CartSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     items = CartItemSerializer(read_only=True)
#
#     class Meta:
#         model = Cart
#         fields = ['id', 'user', 'items']

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CategorySerializer(serializers.ModelSerializer):
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

    def create(self, validated_data):
        category = Category.objects.get(pk=validated_data['category_id'])
        return Product.objects.create(category=category, **validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.price = validated_data.get('price', instance.price)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance


class CartItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
