from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    """_summary_

    This serializer is used to validate and serialize the data required for registering a new user.
    """
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
        ]

    def create(self, validated_data):
        
        user = User.objects.create_user(**validated_data)
        
        return user

class LoginSerializer(serializers.Serializer):
    """_summary_

    This serializer is used to validate the credentials (username and password) provided by a user
    during the login process.
    """
    username = serializers.CharField()
    password = serializers.CharField()