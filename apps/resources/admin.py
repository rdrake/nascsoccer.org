from django.contrib import admin

from .models import Park, Location

class ParkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Park, ParkAdmin)
admin.site.register(Location, LocationAdmin)
