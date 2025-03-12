from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """Serializer for Contributor login"""
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)