from django.contrib.gis.db import models
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

#===================model for hospital registration ============================
class Hospital(models.Model):
    name = models.CharField(max_length=255) 
    location = models.PointField()
    address = models.TextField()

