from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from projectmanagement.models import Contributor, Address
from projectmanagement.serializers.addressSerializers import AddressSerializer


class ContributorSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    """Serializer for Contributor registration"""
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Hash password
        return super().create(validated_data)

    class Meta:
        model = Contributor
        fields = "__all__"

    def create(self, validated_data):
        address_data = validated_data.pop('address')  # Extract address data
        address = Address.objects.create(**address_data)  # Create Address object
        contributor = Contributor.objects.create(address=address, **validated_data)  # Create Contributor
        return contributor

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')  # Extract address data
        instance.address.streetNumber = address_data.get('streetNumber', instance.address.streetNumber)
        instance.address.postalCode = address_data.get('postalCode', instance.address.postalCode)
        instance.address.city = address_data.get('city', instance.address.city)
        instance.address.country = address_data.get('country', instance.address.country)
        instance.address.save()

        instance.fullName = validated_data.get('fullName', instance.fullName)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance