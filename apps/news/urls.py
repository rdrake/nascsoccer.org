from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns("",
    url(
        r"^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\d\-]+)/$",
        ItemDetailView.as_view(),
        name="news_item"
    ),
    url(
        r"^$",
        ItemListView.as_view(),
        name="news"
    )
)
