from django.db import models

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
        ordering = ["-created_at"]
