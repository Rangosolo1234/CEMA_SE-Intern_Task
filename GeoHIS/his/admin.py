from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Hospital, HealthProgram, DoctorProfile, Client, Booking, BlogPost, Incidence

# Register your models here.
@admin.register(Hospital)
class HospitalAdmin(LeafletGeoAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)

@admin.register(HealthProgram)
class HealthProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_description')
    search_fields = ('user__username',)

@admin.register(Client)
class ClientAdmin(LeafletGeoAdmin):
    list_display = ('first_name', 'last_name', 'age')
    search_fields = ('first_name', 'last_name')

@admin.register(Booking)
class BookingAdmin(LeafletGeoAdmin):
    list_display = ('client', 'doctor', 'appointment_time', 'is_home_visit', 'cost')
    search_fields = ('client__first_name', 'doctor__user__username')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    search_fields = ('title', 'author__username')
    list_filter = ('category',)

@admin.register(Incidence)
class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('program', 'reported_by', 'reported_at')
    search_fields = ('program__name', 'reported_by__username')