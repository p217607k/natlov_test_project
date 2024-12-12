from django.contrib.auth import authenticate
from .serializers  import UserSerializer
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework import status

# Create your views here.


class UserRegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Serialize the incoming data
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save the user
        user = serializer.save()
        
        # Send a welcome email asynchronously
        
        
        # Respond with success message and user data
        return Response(
            {
                "message": "User registered successfully.",
                "user": serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    
class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
       
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            
            user = User.objects.get(email=email)
            user = authenticate(username=user.username, password=password)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        if user is not None:
            return Response(
                {
                    "message": "Login successful.",
                    
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                    },
                },
                status=status.HTTP_200_OK,
            )
        else:
            # Invalid credentials
            return Response(
                {"error": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
