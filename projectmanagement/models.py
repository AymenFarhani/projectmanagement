from django.db import models

# class model
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    startDate = models.DateField()
