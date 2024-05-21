from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField(source = "User.created_at")
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "created_at", "is_seller"]