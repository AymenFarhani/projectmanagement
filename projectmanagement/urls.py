from django.urls import path
from . import views

#mapping views methods to there urls
urlpatterns = [
    path('projects', views.getProjects, name='getProjects'),
    path('project/<int:pk>', views.getProject, name='getProject'),
    path('projects/create', views.createProject, name='createProject'),
    path('projects/<int:pk>/update', views.updateProject, name='updateProject'),
    path('projects/<int:pk>/delete', views.deleteProject, name='deleteProject'),

    # Contributor URLs
    path('contributors/', views.getContributors, name="getContributors"),
    path('contributors/<int:pk>/', views.getContributor, name="getContributor"),
    path('contributors/create/', views.createContributor, name="createContributor"),
    path('contributors/update/<int:pk>/', views.updateContributor, name="updateContributor"),
    path('contributors/delete/<int:pk>/', views.deleteContributor, name="deleteContributor"),
]