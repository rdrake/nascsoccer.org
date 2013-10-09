import os, os.path

import dj_database_url

ADMINS = (
	("Richard Drake", "richard.drake@nascsoccer.org"),
)

SECRET_KEY = os.environ.get("SECRET_KEY")

DATABASES = {
	"default": dj_database_url.config(default="postgres://localhost/schedule"),
}

SOUTH_DATABASE_ADAPTERS = {
	"default": "south.db.postgresql_psycopg2"
}

MANAGERS = ADMINS

DJANGO_ROOT = os.path.dirname(
	os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

SITE_ROOT = os.path.dirname(DJANGO_ROOT)
SITE_NAME = "Oshawa N.A.S.C. Soccer"

ALLOWED_HOSTS = []
TIME_ZONE = "America/Toronto"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = False
USE_L10N = True
USE_TZ = True

TIME_FORMAT = "h:i A"

MEDIA_ROOT = os.path.normpath(os.path.join(DJANGO_ROOT, "public", "media"))
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.normpath(os.path.join(DJANGO_ROOT, "public", "static"))
STATIC_URL = "/static/"

STATICFILES_DIRS = (
	os.path.join(DJANGO_ROOT, "project", "static"),
)

STATICFILES_FINDERS = (
	"django.contrib.staticfiles.finders.FileSystemFinder",
	"django.contrib.staticfiles.finders.AppDirectoriesFinder",
	"compressor.finders.CompressorFinder",
)

TEMPLATE_LOADERS = (
	"django_haml.filesystem.Loader",
	"django_haml.app_directories.Loader",
	"django.template.loaders.filesystem.Loader",
	"django.template.loaders.app_directories.Loader",
)

MIDDLEWARE_CLASSES = (
	"django.middleware.common.CommonMiddleware",
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
	"django.middleware.gzip.GZipMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	#"django.core.context_processors.i18n",
	"django.core.context_processors.request",
	"django.core.context_processors.media",
	"django.core.context_processors.static",
)

ROOT_URLCONF = "project.urls"

WSGI_APPLICATION = "project.wsgi.application"

TEMPLATE_DIRS = (
	os.path.normpath(os.path.join(DJANGO_ROOT, "templates")),
)

INSTALLED_APPS = (
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.sites",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	"django.contrib.humanize",
	"django.contrib.flatpages",
	"leaflet",
	"mptt",
	"apps.common",
	"apps.resources",
	"apps.schedule",
	"apps.cms",
	"apps.news",
	"filer",
	"easy_thumbnails",
	"django.contrib.admin",
	"south",
	"django_extensions",
)

LOGGING = {
	"version": 1,
	"disable_existing_loggers": False,
	"filters": {
		"require_debug_false": {
			"()": "django.utils.log.RequireDebugFalse"
		}
	},
	"handlers": {
		"mail_admins": {
			"level": "ERROR",
			"filters": ["require_debug_false"],
			"class": "django.utils.log.AdminEmailHandler"
		}
	},
	"loggers": {
		"django.request": {
			"handlers": ["mail_admins"],
			"level": "ERROR",
			"propagate": True,
		},
	}
}

INTERNAL_IPS = ("127.0.0.1",)

LEAFLET_CONFIG = {
	"TILES": "http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
	"SCALE": False,
	"MINIMAP": False,
}

CACHES = {
	"default": {
		"BACKEND": "redis_cache.RedisCache",
		"LOCATION": "/tmp/redis.sock",
	}
}

BROKER_URL = "redis://"
