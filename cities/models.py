from django.db import models
# cities/models.py
from django.db import models


class City(models.Model):
    zipcode = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    therapy_type = models.CharField(max_length=300)
    resource_type = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    sexuality = models.CharField(max_length=255)
    condition = models.CharField(max_length=255) 
    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name
# Create your models here.
