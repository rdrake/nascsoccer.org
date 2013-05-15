from datetime import timedelta

from django.db.models import Q
from django.shortcuts import get_object_or_404

from django_ical.views import ICalFeed

from .models import Game, Team, Competition

class GameFeed(ICalFeed):
    def get_object(self, request, competition, age_group, team):
        self.competition = get_object_or_404(Competition, slug=competition)
        self.team = get_object_or_404(Team, age_group__slug=age_group, slug=team)

        return self.team;

    def title(self, obj):
        return "%s Games for %s %s" % (
            self.competition.name,
            obj.age_group.name,
            obj.name
        )

    def link(self, obj):
        return "/schedule/%s/%s/%s/" % (
            self.competition.slug,
            obj.age_group.slug,
            obj.slug
        )

    def items(self, obj):
        return Game.objects.filter(
            Q(home_team=obj) | Q(away_team=obj),
            competition=self.competition,
        )

    def item_link(self, obj):
        return "/schedule/%s/%s/%s/" % (
            self.competition.slug,
            obj.age_group.slug,
            self.team.slug
        )

    def item_class(self, obj):
        return "PUBLIC"
    
    def item_location(self, obj):
        return obj.location.name

    def item_geolocation(self, obj):
        return (obj.location.lat, obj.location.lng)

    def item_start_datetime(self, item):
        return item.when

    def item_end_datetime(self, item):
        return item.when + timedelta(hours=1)
    
    def item_guid(self, item):
        return "%d-%d-%d-%d@nascsoccer.org" % (
            self.competition.id,
            item.age_group.id,
            self.team.id,
            item.id
        )
