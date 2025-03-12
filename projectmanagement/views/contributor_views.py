from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Contributor
from ..serializers import ContributorSerializer


# Get all contributors
@api_view(['GET'])
@login_required
def getContributors(request):
    contributors = Contributor.objects.all()
    serializer = ContributorSerializer(contributors, many=True)
    return Response(serializer.data)


# Get a single contributor by ID
@api_view(['GET'])
@login_required
def getContributor(request, email):
    try:
        contributor = Contributor.objects.get(email=email)
    except Contributor.DoesNotExist:
        return Response({'error': 'Contributor not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ContributorSerializer(contributor)
    return Response(serializer.data)


# Create a new contributor
@api_view(['POST'])
@login_required
def createContributor(request):
    serializer = ContributorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Update a contributor by ID
@api_view(['PUT'])
@login_required
def updateContributor(request, pk):
    try:
        contributor = Contributor.objects.get(pk=pk)
    except Contributor.DoesNotExist:
        return Response({'error': 'Contributor not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ContributorSerializer(contributor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete a contributor by ID
@api_view(['DELETE'])
@login_required
def deleteContributor(request, email):
    try:
        contributor = Contributor.objects.get(email=email)
    except Contributor.DoesNotExist:
        return Response({'error': 'Contributor not found'}, status=status.HTTP_404_NOT_FOUND)

    contributor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
