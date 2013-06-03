from collections import defaultdict

from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import Game, Competition, AgeGroup, Team

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

class StandingsList(GameList):
    template_name = "schedule/standings_list.html"

    def _compute_standings(self, context):
        key = "%s:%s" % (context["age_group"].name, context["competition"].name)

        if cache.get(key) is None:
            standings = defaultdict(dict)

            # Handle the case where no standings exist.
            for team in Team.objects.filter(age_group=context["age_group"]):
                for stat in "gf ga gd wins ties losses points".split():
                    standings[team][stat] = 0

            for game in context["object_list"]:
                if game.home_score != None and game.away_score != None:
                    winner = None
                    loser = None

                    goals_diff = game.home_score_norm - game.away_score_norm

                    if goals_diff > 0:
                        winner = game.home_team
                        loser = game.away_team
                    elif goals_diff < 0:
                        winner = game.away_team
                        loser = game.home_team

                    if winner:
                        standings[winner]["wins"] += 1
                        standings[winner]["points"] += 3
                        if not game.bye:
                            standings[loser]["losses"] += 1
                    else:
                        for team in [game.home_team, game.away_team]:
                            standings[team]["ties"] += 1
                            standings[team]["points"] += 1

                    standings[game.home_team]["gf"] += game.home_score_norm
                    standings[game.home_team]["ga"] += game.away_score_norm

                    if not game.bye:
                        standings[game.away_team]["gf"] += game.away_score_norm
                        standings[game.away_team]["ga"] += game.home_score_norm
            
            for team, stats in standings.iteritems():
                standings[team]["gd"] = standings[team]["gf"] - standings[team]["ga"]

            # Place the standings in the cache for 10 minutes
            cache.set(key, dict(standings), 60 * 10)

        return cache.get(key)

    def get_context_data(self, **kwargs):
        context = super(StandingsList, self).get_context_data(**kwargs)

        context["standings"] = self._compute_standings(context)

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
