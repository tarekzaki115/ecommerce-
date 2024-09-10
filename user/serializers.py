from rest_framework import serializers, exceptions
from .models import *
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from dj_rest_auth.serializers import LoginSerializer
from allauth.account.adapter import get_adapter

class UserSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField(source = "User.created_at")
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "created_at", "is_seller"]


class CustomerLoginSerializer(LoginSerializer):
    username = None

    def authenticate(self, **options):
        return authenticate(self.context["request"], **options)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        if email and password:
            user = authenticate(
                email=email,
                password=password,
            )
            if not user:
                msg = "Incorrect credentials."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = "No email provided."
            raise exceptions.ValidationError(msg)
        attrs["user"] = user
        return attrs