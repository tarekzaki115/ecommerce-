from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

from .views import *

CartsItemsList =  CartItemViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

CartItemDetail = CartItemViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

CartsList =  CartViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

CartDetail = CartViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

ItemList = ItemViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

ItemDetail = ItemViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

CategoryList = CategoryViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)
CategoryDetail = CategoryViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

urlpatterns = [
    path("items/", ItemList, name="ItemList"),
    path("items/<int:pk>/", ItemDetail, name = "ItemDetail"),
    path("carts/", CartsList, name = "CartsList"),
    path("carts/<int:pk>/", CartDetail, name = "CartDetail"),
    path("cartItems/", CartsItemsList, name = "CartItemsList"),
    path("cartItems/<int:pk>/", CartItemDetail, name = "CartItemDetail"),
    path("Categories/", CategoryList, name = "CategoryList"),
    path("Categories/<int:pk>/", CategoryDetail, name = "CategoryDetail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

