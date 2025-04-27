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

#================Booking session model============
class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    is_home_visit = models.BooleanField(default=False)
    location = models.PointField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    appointment_time = models.DateTimeField()


#===================Blog post model================
class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('educational', 'Educational'),
        ('inspirational', 'Inspirational'),
        ('research', 'Research'),
        ('incidences', 'Incidences'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    program = models.ForeignKey(HealthProgram, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

#==================Model for incidence report==============
class Incidence(models.Model):
    program = models.ForeignKey(HealthProgram, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.PointField()
    reported_at = models.DateTimeField(auto_now_add=True)