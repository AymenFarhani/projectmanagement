from rest_framework import serializers

from projectmanagement.models import Project
from projectmanagement.serializers.contributorSerializers import ContributorSerializer


class ProjectSerializer(serializers.ModelSerializer):
    contributors = ContributorSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = '__all__'