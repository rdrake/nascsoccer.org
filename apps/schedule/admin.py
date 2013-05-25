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

class GameAdmin(admin.ModelAdmin):
    list_display = ("age_group", "competition", "when", "home_team", "home_score", "away_team", "away_score", "location", "bye")
    list_filter = ("age_group", "competition")

    def queryset(self, request):
        # TODO:  Changed to get_queryset(self, request) in dev (> 1.5).
        qs = super(GameAdmin, self).queryset(request)
        qs = qs.select_related("age_group__name", "competition__name", "home_team__name", "away_team__name", "location__name")

        return qs

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(AgeGroup, AgeGroupAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Game, GameAdmin)
