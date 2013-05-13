from django.contrib import admin
from .models import AgeGroup, Team, Competition, Game

class AgeGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("age_group", "park", "name")
    list_filter = ("age_group",)

class CompetitionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(AgeGroup, AgeGroupAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Game)
