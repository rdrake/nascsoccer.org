from django.conf.urls import patterns, include, url

from .views import CompetitionList, GameList, AgeGroupList, ParkList, ParkDetailView, LocationList, LocationDetailView, TeamGameList

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
   # Examples:
   # url(r"^$", "schedule.views.home", name="home"),
   # url(r"^schedule/", include("schedule.foo.urls")),

   # Uncomment the admin/doc line below to enable admin documentation:
   # url(r"^admin/doc/", include("django.contrib.admindocs.urls")),

   # Uncomment the next line to enable the admin:
   (r"^grappelli/", include("grappelli.urls")),
   url(r"^admin/", include(admin.site.urls)),
   (r"^api/v2/", include("fiber.rest_api.urls")),
   (r"^admin/fiber/", include("fiber.admin_urls")),
   (r"^jsi18n/$", "django.views.i18n.javascript_catalog", {"packages": ("fiber",),}),
)

# Schedules
urlpatterns += patterns("",
  url(r"^schedule/$", CompetitionList.as_view(), name="competition"),
  url(r"^schedule/(?P<competition>[\w\d-]+)/$", AgeGroupList.as_view(), name="age_group"),
  url(r"^schedule/(?P<competition>[\w\d-]+)/(?P<age_group>[\w\d-]+)/$", GameList.as_view(), name="schedule"),
  url(r"^schedule/(?P<competition>[\w\d-]+)/(?P<age_group>[\w\d-]+)/(?P<team>[\w\d-]+)/$", TeamGameList.as_view(), name="team_schedule"),
)

# Parks
urlpatterns += patterns("",
  url(r"^park/$", ParkList.as_view(), name="parks"),
  url(r"^park/(?P<slug>[\w\d-]+)/$", ParkDetailView.as_view(), name="park"),
)

# Locations
urlpatterns += patterns("",
  url(r"^location/$", LocationList.as_view(), name="locations"),
  url(r"^location/(?P<slug>[\w\d-]+)/$", LocationDetailView.as_view(), name="location"),
)

# Must add django-fiber afterwards as it assumes direct control.
urlpatterns += patterns("",
  (r"", "fiber.views.page"),
)
