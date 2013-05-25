from django.conf.urls import patterns, url

from .feeds import *
from .views import *

urlpatterns = patterns("",
    url(r"^$", CompetitionList.as_view(), name="competition"),
    url(
        r"^(?P<competition>[\w\d-]+)/$",
        AgeGroupList.as_view(),
        name="age_group"
    ),
    url(
        r"^(?P<competition>[\w\d-]+)/(?P<age_group>[\w\d-]+)/$",
        GameList.as_view(),
        name="schedule"
    ),
    url(
        r"^(?P<competition>[\w\d-]+)/(?P<age_group>[\w\d-]+)/standings/$",
        StandingsList.as_view(),
        name="standings"
    ),
    url(
        r"^(?P<competition>[\w\d-]+)/(?P<age_group>[\w\d-]+)/(?P<team>[\w\d-]+)/$",
        TeamGameList.as_view(),
        name="team_schedule"
    ),
    url(
        r"^(?P<competition>[\w\d-]+)/(?P<age_group>[\w\d-]+)/(?P<team>[\w\d-]+)/ical/$",
        GameFeed(),
        name="team_schedule_feed"
    ),
)
