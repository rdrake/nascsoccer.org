from django.db import models

class NamedEntity(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  slug = models.SlugField()

  def __unicode__(self):
    return self.name

  class Meta:
    abstract = True

class AgeGroup(NamedEntity):
  standings = models.BooleanField(default=True)

  class Meta:
    ordering = ["name"]

class Team(NamedEntity):
  park = models.ForeignKey("Park")
  age_group = models.ForeignKey(AgeGroup)

  def __unicode__(self):
    return "%s - %s" % (self.age_group.name, self.name)

  class Meta:
    ordering = ["park__name", "name"]

class Park(NamedEntity):
  founded = models.IntegerField(blank=True, null=True)
  logo = models.ImageField(upload_to="park_logos", blank=True, null=True)
  
  class Meta:
    ordering = ["name"]

class Location(NamedEntity):
  lat = models.FloatField(blank=True, null=True)
  lng = models.FloatField(blank=True, null=True)

  class Meta:
    ordering = ["name"]

class Competition(NamedEntity):
  age_groups = models.ManyToManyField(AgeGroup)

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
    ordering = ["id"]
