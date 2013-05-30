from django.db import models
from django.core.urlresolvers import reverse

from filer.fields.image import FilerImageField

from apps.common.models import NamedEntity

class Park(NamedEntity):
    founded = models.IntegerField(blank=True, null=True)
    logo = FilerImageField(blank=True, null=True)
    
    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("park", kwargs={"slug": self.slug})

class Location(NamedEntity):
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    status = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("location", kwargs={"slug": self.slug})
