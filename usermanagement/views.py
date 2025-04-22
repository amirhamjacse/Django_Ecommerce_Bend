from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser, AllowAny
)
from django.contrib.auth import authenticate, login
from .models import User, Role
from .serializers import (
    UserSerializer, UserCreateSerializer,
    LoginSerializer, ForgotPasswordSerializer,
    ResetPasswordSerializer, AddUserSerializer
)
from django.core.mail import send_mail
from django.utils.timezone import now, timedelta
from django.contrib.auth.hashers import make_password
import random
from drf_yasg.utils import swagger_auto_schema

# User = get_user_model()
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterUser(APIView):
    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            if 'role' not in serializer.validated_data:
                user_role = Role.objects.get(name='User')
                serializer.validated_data['role'] = user_role
            serializer.save()
            return Response(
                {"status": True, "message": "User created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginUser(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            # Manually authenticate the user using email
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    if user.is_active:
                        refresh = RefreshToken.for_user(user)
                        access_token = str(refresh.access_token)
                        refresh_token = str(refresh)
                        login(request, user)  # Optional: Only for session-based authentication
                        return Response(
                            {"status": True,
                              "message": "Login successful",
                              "access_token": access_token,
                              "refresh_token": refresh_token,
                              }
                        )
                    else:
                        return Response(
                            {"status": False, "message": "User is not active"},
                            status=status.HTTP_401_UNAUTHORIZED
                        )
                else:
                    return Response(
                        {"status": False, "message": "Invalid credentials"},
                        status=status.HTTP_401_UNAUTHORIZED
                    )
            except User.DoesNotExist:
                return Response(
                    {"status": False, "message": "User does not exist"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllUsers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(
            {"status": True, "message": "Users fetched successfully", "data": serializer.data})


class ForgotPassword(APIView):
    @swagger_auto_schema(request_body=ForgotPasswordSerializer)
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)

            # Generate OTP
            otp = str(random.randint(100000, 999999))
            user.otp = otp
            print(otp, 'otp-----')

            user.otp_expired_at = now() + timedelta(minutes=10)  # OTP valid for 10 minutes
            user.save()

            # Send OTP via email (Update with your SMTP settings)
            send_mail(
                subject="Your Password Reset OTP",
                message=f"Your OTP for password reset is: {otp}. It will expire in 10 minutes.",
                from_email="media.amirhamja@gmail.com",
                recipient_list=[user.email],
                fail_silently=False,
            )
            print('works ---')
            

            return Response({"status": True, "message": "OTP sent successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPassword(APIView):
    @swagger_auto_schema(request_body=ResetPasswordSerializer)
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = User.objects.get(email=email)
            user.password = make_password(password)
            user.otp = None 
            user.otp_expired_at = None
            user.save()

            return Response({"status": True, "message": "Password reset successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddUser(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=AddUserSerializer)
    def post(self, request):
        serializer = AddUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "message": "User created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUser(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(request_body=UserSerializer)
    def put(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(
                {"status": False, "message": "User not found"},
                status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "message": "User updated successfully", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUser(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(
                {"status": False, "message": "User not found"},
                status=status.HTTP_404_NOT_FOUND)


        user.delete()
        return Response({"status": True, "message": "User deleted successfully"})
