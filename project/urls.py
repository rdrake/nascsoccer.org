from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns("",
    (r"^$", include("apps.common.urls")),
    url(r"^admin/", include(admin.site.urls)),
    (r"^schedule/", include("apps.schedule.urls")),
    (r"^resources/", include("apps.resources.urls")),
    (r"^news/", include("apps.news.urls")),
)

# Serve media files in debug mode.
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
