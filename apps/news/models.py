from django.db import models
from django.core.urlresolvers import reverse

class Item(models.Model):
    title = models.CharField(max_length=255)

    slug = models.SlugField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    content = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-updated_at"]

    def get_absolute_url(self):
        return reverse("news_item", kwargs={
            "year": self.updated_at.year,
            "month": self.updated_at.month,
            "slug": self.slug
        })
