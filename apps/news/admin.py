from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Item, ItemAdmin)
