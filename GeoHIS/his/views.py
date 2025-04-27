from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

#===============view for hospitals =============
class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

#==============view for health programs =============
class HealthProgramViewSet(viewsets.ModelViewSet):
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer

#===========view for doctor profiles ==================
class DoctorProfileViewSet(viewsets.ModelViewSet):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer

#=========== View for clients profies==============
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

#===========view for appointment boking============
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

#=================view for blog posts ==============
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

#===================view for incidences==============
class IncidenceViewSet(viewsets.ModelViewSet):
    queryset = Incidence.objects.all()
    serializer_class = IncidenceSerializer