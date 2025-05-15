from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegisterUser(APIView):
    def post(self, request, *args, **kwargs):
        # Extracting data from the request
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        confirm_password = request.data.get("confirmPassword")

        # Password match check
        if password != confirm_password:
            return Response(
                {"error": "Passwords do not match"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already taken"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "Email already taken"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Password validation (optional, but good practice)
        try:
            validate_password(password)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create the user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return Response(
                {"message": "User created successfully"},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
