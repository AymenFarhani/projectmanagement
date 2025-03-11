from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Project
from .serializers import ProjectSerializer

# the controller class


#Get all projects
@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

#get single project by Id
@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(pk=pk)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)

#create project
@api_view(['POST'])
def createProject(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])

#update project by Id
def updateProject(request, pk):
    project = Project.objects.get(pk=pk)
    serializer = ProjectSerializer(project, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#delete project by Id
@api_view(['DELETE'])
def deleteProject(request, pk):
    project = Project.objects.get(pk=pk)
    project.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
