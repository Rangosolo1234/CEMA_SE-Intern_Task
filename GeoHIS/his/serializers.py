# serializers.py
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Hospital, HealthProgram, DoctorProfile, Client, Booking, BlogPost, Incidence

class HospitalSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'address', 'location']
        geo_field = 'location'

class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = ['id', 'name', 'created_at']

class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ['user', 'short_description']

class ClientSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'age', 'location']
        geo_field = 'location'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'client', 'doctor', 'appointment_time', 'is_home_visit', 'cost']

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'author', 'category', 'created_at']

class IncidenceSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Incidence
        fields = ['id', 'program', 'reported_by', 'reported_at', 'location']
        geo_field = 'location'
