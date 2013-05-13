from django.db.models import Q
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404
from django.conf import settings

from .models import Game, Competition, AgeGroup, Park, Location, Team

class GameList(ListView):
  model = Game

  def get_queryset(self):
    self.age_group = get_object_or_404(AgeGroup, slug=self.kwargs["age_group"])
    self.competition = get_object_or_404(Competition, slug=self.kwargs["competition"])

    return Game.objects.filter(competition=self.competition, age_group=self.age_group).select_related("home_team", "away_team", "location")

  def get_context_data(self, **kwargs):
    context = super(GameList, self).get_context_data(**kwargs)

    context["age_group"] = self.age_group
    context["competition"] = self.competition
    context["title"] = " | ".join([self.age_group.name, self.competition.name])

    return context

class TeamGameList(GameList):
  def get_queryset(self):
    queryset = super(TeamGameList, self).get_queryset()
    self.team = get_object_or_404(Team, slug=self.kwargs["team"], age_group=self.age_group)

    return queryset.filter(Q(home_team=self.team) | Q(away_team=self.team))

  def get_context_data(self, **kwargs):
    context = super(TeamGameList, self).get_context_data(**kwargs)

    context["team"] = self.team
    context["title"] = " | ".join([self.team.name, self.age_group.name, self.competition.name])

    return context

class AgeGroupList(ListView):
  model = AgeGroup

  def get_queryset(self):
    self.competition = get_object_or_404(Competition, slug=self.kwargs["competition"])

    return AgeGroup.objects.filter(competition=self.competition)

  def get_context_data(self, **kwargs):
    context = super(AgeGroupList, self).get_context_data(**kwargs)

    context["competition"] = self.competition
    context["title"] = self.competition.name

    return context

class CompetitionList(ListView):
  model = Competition

  def get_context_data(self, **kwargs):
    context = super(CompetitionList, self).get_context_data(**kwargs)
    
    context["title"] = "Schedules"

    return context

class ParkList(ListView):
  model = Park

class ParkDetailView(DetailView):
  model = Park

class LocationList(ListView):
  model = Location

class LocationDetailView(DetailView):
  model = Location
