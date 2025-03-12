from django.urls import path
from . import views
from .views.authentication_views import RegisterContributorView, LoginContributorView

#mapping views methods to there urls
urlpatterns = [
    path('projects', views.getProjects, name='getProjects'),
    path('project/<str:title>', views.getProject, name='getProject'),
    path('projects/create', views.createProject, name='createProject'),
    path('projects/<str:title>/update', views.updateProject, name='updateProject'),
    path('projects/<str:title>/delete', views.deleteProject, name='deleteProject'),

    # Contributor URLs
    path('contributors/', views.getContributors, name="getContributors"),
    path('contributors/<str:email>/', views.getContributor, name="getContributor"),
    path('contributors/create/', views.createContributor, name="createContributor"),
    path('contributors/update/<int:pk>/', views.updateContributor, name="updateContributor"),
    path('contributors/delete/<str:email>/', views.deleteContributor, name="deleteContributor"),

    path('register/', RegisterContributorView.as_view(), name='register'),
    path('login/', LoginContributorView.as_view(), name='login'),
]