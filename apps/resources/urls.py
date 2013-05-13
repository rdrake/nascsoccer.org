from django.conf.urls import patterns, url

from .views import *

# Parks
urlpatterns = patterns("",
    url(
        r"^park/$",
        ParkList.as_view(),
        name="parks"
    ),
    url(
        r"^park/(?P<slug>[\w\d-]+)/$",
        ParkDetailView.as_view(),
        name="park"
    ),
)

# Locations
urlpatterns += patterns("",
    url(
        r"^location/$",
        LocationList.as_view(),
        name="locations"
    ),
    url(
        r"^location/(?P<slug>[\w\d-]+)/$",
        LocationDetailView.as_view(),
        name="location"
    ),
)

