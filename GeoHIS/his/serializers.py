from rest_framework import serializers
from .models import Hospital, HealthProgram, DoctorProfile, Client, Booking, BlogPost, Incidence
from django.contrib.auth.models import User

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class HealthProgramSerializer(serializers.ModelSerializer):
    hospitals = HospitalSerializer(many=True, read_only=True)
    class Meta:
        model = HealthProgram
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class DoctorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = DoctorProfile
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class IncidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidence
        fields = '__all__'