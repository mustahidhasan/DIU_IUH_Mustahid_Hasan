from django.contrib import admin
from .models import bus_details, bus_route, bus_fare
# Register your models here.

admin.site.register(bus_details)
admin.site.register(bus_route)
admin.site.register(bus_fare)