from django.db import models

from projectmanagement.models.contributor import Contributor


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    startDate = models.DateField()
    contributors = models.ManyToManyField(Contributor, related_name='projects')