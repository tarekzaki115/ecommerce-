from rest_framework import permissions

class IsSellerOrAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.seller == request.user or request.user.is_superuser
    
class IsMarkedSeller(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.seller == True
    
"""we will need to create an identical class for obj.cart.user for the item detail update"""

class IsCustomerOrAdminReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        try:
            return obj.cart.customer == request.user or request.user.is_superuser
        except AttributeError:
            return obj.customer == request.user
