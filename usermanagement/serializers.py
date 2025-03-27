from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Role
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User
from django.utils.timezone import now
import random

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'role',
            'full_name',
            'status',
            'phone_number',
            'address',
            'company_id'
            ]


class UserCreateSerializer(serializers.ModelSerializer):
    # full_name = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'role',
            'full_name',
            'status',
            'phone_number',
            'address',
            'company_id'
            ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": "Invalid email address."})

        if user.otp != data["otp"]:
            raise serializers.ValidationError({"otp": "Invalid OTP."})

        if user.otp_expired_at and user.otp_expired_at < now():
            raise serializers.ValidationError({"otp": "OTP has expired."})

        return data

# class ForgotPasswordSerializer(serializers.Serializer):
#     email = serializers.EmailField()


# class ResetPasswordSerializer(serializers.Serializer):
#     password = serializers.CharField()



from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Role

class AddUserSerializer(serializers.ModelSerializer):
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), source='role', write_only=True, required=False
    )  # Accept role ID but optional

    class Meta:
        model = User
        fields = [
            "id", "username", "email", "password", "full_name", "status",
            "phone_number", "address", "company_id", "role", "role_id",
            "otp", "otp_expired_at",
        ]
        extra_kwargs = {
            "password": {"write_only": True},  # Hide password in response
            # "created_at": {"read_only": True},
            # "updated_at": {"read_only": True},
        }

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])  # Hash password
        return super().create(validated_data)
