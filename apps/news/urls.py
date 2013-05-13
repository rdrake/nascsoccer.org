from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns("",
    url(
        r"^(?P<slug>[\w\d\-]+)/$",
        ItemDetailView.as_view(),
        name="news"
    ),
)
