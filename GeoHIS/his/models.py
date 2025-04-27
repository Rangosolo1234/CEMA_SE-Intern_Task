from django.contrib.gis.db import models
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

#===================model for hospital registration ============================
class Hospital(models.Model):
    name = models.CharField(max_length=255) 
    location = models.PointField()
    address = models.TextField()

#==================model to register a ealth program=================
class HealthProgram(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    hospitals = models.ManyToManyField(Hospital)


#===============Doctors profile=========================================
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualifications = models.TextField()
    short_description = models.TextField()
    programs_responsible = models.ManyToManyField(HealthProgram, related_name='doctors')

#================Client=====================
class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    location = models.PointField()
    health_history = models.TextField()
    age = models.PositiveIntegerField()
    programs_joined = models.ManyToManyField(HealthProgram)
    registered_by = models.ForeignKey(DoctorProfile, null=True, blank=True, on_delete=models.SET_NULL)