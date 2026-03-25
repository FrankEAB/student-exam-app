from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer
from .models import Profile


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            tokens = get_tokens_for_user(user)


            profile = Profile.objects.get(user=user)

            return Response({
                "message": "User registered successfully",
                "tokens": tokens,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "student_id": profile.student_id
                }
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):

        identifier = (
            request.data.get("username") or
            request.data.get("email") or
            request.data.get("student_id")
        )
        password = request.data.get("password")

        if not identifier or not password:
            return Response(
                {"error": "Please provide your Email/Student ID and password."},
                status=status.HTTP_400_BAD_REQUEST
            )


        user = authenticate(request, username=identifier, password=password)

        if user is not None:
            tokens = get_tokens_for_user(user)
            profile = Profile.objects.get(user=user)

            return Response({
                "message": "Login successful",
                "tokens": tokens,
                "user": {
                    "full_name": profile.full_name,
                    "email": user.email,
                    "student_id": profile.student_id
                }
            }, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid credentials. Please check your Student ID/Email and password."},
            status=status.HTTP_401_UNAUTHORIZED
        )