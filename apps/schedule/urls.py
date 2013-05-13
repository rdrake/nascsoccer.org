from django.conf.urls import patterns, url

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
        r"^(?P<competition>[\w\d-]+)/(?P<age_group>[\w\d-]+)/(?P<team>[\w\d-]+)/$",
        TeamGameList.as_view(),
        name="team_schedule"
    ),
)
