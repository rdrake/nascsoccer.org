from django.db import models

from filer.fields.image import FilerImageField

from apps.common.models import NamedEntity

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
