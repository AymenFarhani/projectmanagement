from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Project
from ..serializers import ProjectSerializer
import openpyxl

# The controller class


#Get all projects
@api_view(['GET'])
@login_required
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

#get single project by title
@api_view(['GET'])
@login_required
def getProject(request,title):
    project = Project.objects.get(title=title)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)

#create project
@api_view(['POST'])
@login_required
def createProject(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#update project by Id
@api_view(['PUT'])
@login_required
def updateProject(request, title):
    project = Project.objects.get(title=title)
    serializer = ProjectSerializer(project, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#delete project by Id
@api_view(['DELETE'])
@login_required
def deleteProject(request, title):
    project = Project.objects.get(title=title)
    project.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#export all projects in excel format
def get(self, request, *args, **kwargs):
    projects = Project.objects.all()

    # Create a new Excel workbook and add a worksheet
    workBook = openpyxl.Workbook()
    sheet = workBook.active
    sheet.title = 'Projects'

    # Define header
    sheet.append(['ID', 'Title', 'Start Date', 'Contributors'])

    # Add project data to the Excel sheet
    for project in projects:
        contributors = ", ".join([str(contributor) for contributor in project.contributors.all()])
        sheet.append([project.id, project.title, project.startDate, contributors])

    # Prepare the response for file download
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=projects.xlsx'

    # Save the workbook to the response
    workBook.save(response)

    return response
