from django.db import models

from apps.common.models import NamedEntity
from apps.resources.models import Location, Park

MAX_DIFFERENCE = 7

class AgeGroup(NamedEntity):
    standings = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

class Team(NamedEntity):
    park = models.ForeignKey(Park)
    age_group = models.ForeignKey(AgeGroup)

    class Meta:
        ordering = ["park__name", "name"]

class Competition(NamedEntity):
    age_groups = models.ManyToManyField(AgeGroup)

    def get_absolute_url(self):
        return ("age_group", (), {
            "competition": self.slug
        })

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    when = models.DateTimeField()

    age_group = models.ForeignKey(AgeGroup)
    competition = models.ForeignKey(Competition)

    home_team = models.ForeignKey(Team, related_name="home_games", blank=True, null=True)
    away_team = models.ForeignKey(Team, related_name="away_games", blank=True, null=True)

    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)

    location = models.ForeignKey(Location, blank=True, null=True)

    bye = models.BooleanField(default=False)

    class Meta:
        ordering = ["when"]

    def _get_home_score(self):
        difference = self.home_score - self.away_score

        if difference > MAX_DIFFERENCE:
            return self.home_score - difference + MAX_DIFFERENCE
        
        return self.home_score

    def _get_away_score(self):
        difference = self.away_score - self.home_score

        if difference > MAX_DIFFERENCE:
            return self.away_score - difference + MAX_DIFFERENCE 

        return self.away_score

    home_score_norm = property(_get_home_score)
    away_score_norm = property(_get_away_score)
