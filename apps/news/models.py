from django.core.urlresolvers import reverse
from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=255)

    slug = models.SlugField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    content = models.TextField()

    #@models.permalink
    #def get_absolute_url(self):
    #    return reverse("news_item",
    #        kwargs={
    #            "slug": self.slug,
    #            "year": self.updated_at.year,
    #            "month": self.updated_at.month
    #        })
        #return ("news_item", (), {
        #    "slug": self.slug,
        #    "year": self.created_at.year,
        #    "month": self.created_at.month
        #})
