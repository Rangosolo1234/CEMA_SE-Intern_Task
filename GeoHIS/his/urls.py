from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HospitalViewSet, HealthProgramViewSet, DoctorProfileViewSet, ClientViewSet, BookingViewSet, BlogPostViewSet, IncidenceViewSet

router = DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'healthprograms', HealthProgramViewSet)
router.register(r'doctorprofiles', DoctorProfileViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'blogposts', BlogPostViewSet)
router.register(r'incidences', IncidenceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]