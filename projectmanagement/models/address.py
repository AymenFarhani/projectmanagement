from django.db import models

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    streetNumber = models.IntegerField()
    postalCode = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.streetNumber} {self.postalCode} {self.city} {self.country}"
