from django.urls import path
from . import views
#mapping views methods to there urls
urlpatterns = [
    path('', views.getProjects, name='getProjects'),
    path('project/<int:pk>', views.getProject, name='getProject'),
    path('create', views.createProject, name='createProject'),
    path('projects/<int:pk>/update', views.updateProject, name='updateProject'),
    path('projects/<int:pk>/delete', views.deleteProject, name='deleteProject'),

]