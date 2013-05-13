from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import ExtendedFlatPage

admin.site.register(ExtendedFlatPage, MPTTModelAdmin)
