from django.db import models

from projectmanagement.models.address import Address


class Contributor(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fullName} {self.email}"
