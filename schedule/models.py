from django.db import models
from django.contrib.flatpages.models import FlatPage

from mptt.models import MPTTModel, TreeForeignKey
from filer.fields.image import FilerImageField

from .manager import PageManager

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
  logo = FilerImageField(blank=True, null=True)
  
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

class ExtendedFlatPage(MPTTModel, FlatPage):
  parent = TreeForeignKey("self", null=True, blank=True, related_name="children")
  objects = PageManager()

  class Meta:
    ordering = ["flatpages__url"]
    order_with_respect_to = "parent"
    verbose_name = "page"
    verbose_name_plural = "pages"

  class MPTTMeta:
    left_attr = "mptt_left"
    right_attr = "mptt_right"
    level_attr = "mptt_level"
    order_insertion_by = ["title"]

  def is_child_of(self, node):
    """
    Returns True if this is a child of the given node.
    """
    return (self.tree_id == node.tree_id and
      self.mptt_left > node.mptt_left and
      self.mptt_right < node.mptt_right)

  #def get_ancestors(self, *args, **kwargs):
  #  if getattr(self, "_ancestors_retrieved", False):
  #    ancestors = []
  #    node = self

  #    while node.parent_id is not None:
  #      ancestors.insert(0, node.parent)
  #      node = node.parent
  #      
  #      return ancestors
  #  else:
  #    return super(Page, self).get_ancestors(*args, **kwargs)

  def __unicode__(self):
    return self.url
