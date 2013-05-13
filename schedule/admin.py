from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from schedule.models import AgeGroup, Team, Park, Location, Competition, Game, ExtendedFlatPage

class AgeGroupAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}

class TeamAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}
  list_display = ("age_group", "park", "name")
  list_filter = ("age_group",)

class ParkAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}

class LocationAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}

class CompetitionAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}

admin.site.register(AgeGroup, AgeGroupAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Park, ParkAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Game)
admin.site.register(ExtendedFlatPage, MPTTModelAdmin)
