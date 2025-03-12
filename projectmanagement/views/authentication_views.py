from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from ..models.contributor import Contributor
from ..serializers.contributorSerializers import ContributorSerializer
from ..serializers.loginSerializers import LoginSerializer


class RegisterContributorView(generics.CreateAPIView):
    """API endpoint to register a new contributor"""
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user": ContributorSerializer(user).data}, status=status.HTTP_201_CREATED)


class LoginContributorView(generics.GenericAPIView):
    """API endpoint to log in an existing contributor"""
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(email=email, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user": ContributorSerializer(user).data})
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
