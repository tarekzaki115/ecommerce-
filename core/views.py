from functools import partial
from turtle import update
from venv import create
from django.db.migrations import serializer
from django.shortcuts import render

from user.models import User
from user.serializers import UserSerializer
from item.models import *
from item.serializers import *
from item.permissions import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse


"""
   will probably need to create a view for just creating a cart_item instance
   and a cart instance
"""



class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return ItemWriteSerializer
        else:
            return ItemReadOnlySerializer 

    def get_permissions(self):
        
        if self.action in ("create",):
            self.permission_classes = (IsMarkedSeller,)
        elif self.action in ("update", "partial_update", "destroy"):
            self.permission_classes = (IsSellerOrAdminOrReadOnly,)
        else:
            self.permission_classes = (permissions.AllowAny,)
        return super().get_permissions()

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCustomerOrAdminReadOnly]


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = cartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCustomerOrAdminReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = categoriesSerializer
    permission_classes = [permissions.AllowAny]
