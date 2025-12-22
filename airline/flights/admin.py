from django.contrib import admin
from .models import Airport, Flight, Review, Passenger

# Register your models here.
# After creating a super user, we have to change the admin file here 
# we can simply register the model here using admin.site.register(ModelName)
# we manipulate how the admin page looks like using admin.ModelAdmin etc..


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ['code', 'city']
    search_fields = ['city', 'code']

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['id', 'origin', 'destination', 'duration']
    list_filter = ['origin', 'destination']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['flight', 'name', 'rating', 'created']
    list_filter = ['rating', 'created']
    search_fields = ['name', 'comment']

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


