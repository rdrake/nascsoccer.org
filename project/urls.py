from django.conf.urls import patterns, include, url
from schedule.views import CompetitionList, GameList, AgeGroupList, ParkList, ParkDetailView, LocationList, LocationDetailView, TeamGameList, HomeView
from news.views import ItemDetailView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns("",
   # Examples:
   # url(r"^$", "schedule.views.home", name="home"),
   # url(r"^schedule/", include("schedule.foo.urls")),

   # Uncomment the admin/doc line below to enable admin documentation:
   # url(r"^admin/doc/", include("django.contrib.admindocs.urls")),

   # Uncomment the next line to enable the admin:
   url(r"^admin/", include(admin.site.urls)),
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

# News
urlpatterns += patterns("",
  url(r"^news/(?P<slug>[\w\d\-]+)/$", ItemDetailView.as_view(), name="news"),
)

# Home
urlpatterns += patterns("",
  url(r"^$", HomeView.as_view(), name="home")
)
