from dataclasses import field
from email.policy import default
from unicodedata import category
from rest_framework import serializers
from .models import *


class categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= "__all__"



class ItemReadOnlySerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField(source = "Item.created_at")
    seller = serializers.CharField(source = "Item.seller.username", read_only=True)
    category = serializers.CharField(source = "Item.category.category_name", read_only= True)

    class Meta:
        model = Item
        fields = "__all__"

class ItemWriteSerializer(serializers.ModelSerializer):
    #category = categoriesSerializer()
    seller = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Item
        fields = "__all__"

    def create(self, validated_data):
        item = Item.objects.create(**validated_data)
        
        return item

    def update(self, instance, validated_data):
        instance.category = validated_data.get("category", instance.category)
        instance.item_name = validated_data.get("item_name", instance.item_name)
        instance.price = validated_data.get("price", instance.price)
        instance.stock = validated_data.get("stock", instance.stock)
        instance.sold = validated_data.get("sold", instance.sold)
        instance.description = validated_data.get("description", instance.description)
        instance.image = validated_data.get("image", instance.image)
        instance.save()

        return instance

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = cartItem
        fields = "__all__"
        def update(self, instance, validated_data):
            
            instance.quantity = validated_data.get("quantity", instance.quantity)
            instance.item = validated_data.get("item", instance.item)
            instance.cart = validated_data.get("cart", instance.cart)
            instance.save()
            
            return instance


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__" 

    cartitems = CartItemSerializer(many = True)
    def update(self, instance, validated_data):
        instance.customer = validated_data.get("customer", instance.customer)
        instance.save()

        return instance