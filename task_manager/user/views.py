from django.contrib.auth.models import User
from rest_framework import serializers, status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer


class RegisterUserView(views.APIView):
    """_summary_

    This view handles the registration of a new user by accepting the user's data in a POST request.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    'message': 'User registered successfully!',
                    'success':True,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

class LoginView(views.APIView):
    """_summary_

    This view handles the login process by validating the user's credentials (username and password).
    """
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            
            refresh = RefreshToken.for_user(user)
            
            return Response(
                {
                    'message':"Loggin successfull",
                    "success":True,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
            }
            )
        return Response(
            {
                'success':False,
                'error': 'Invalid credentials'
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )