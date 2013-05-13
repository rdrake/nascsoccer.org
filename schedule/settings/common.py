import os.path

ADMINS = (
  ("Richard Drake", "richard.drake@nascsoccer.org"),
)

MANAGERS = ADMINS

DJANGO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE_ROOT = os.path.dirname(DJANGO_ROOT)
SITE_NAME = "Oshawa N.A.S.C. Soccer"

ALLOWED_HOSTS = []
TIME_ZONE = "America/Toronto"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

TIME_FORMAT = "h:i A"

MEDIA_ROOT = os.path.normpath(os.path.join(DJANGO_ROOT, "media"))
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.normpath(os.path.join(DJANGO_ROOT, "static"))
STATIC_URL = "/static/"

STATICFILES_FINDERS = (
  "django.contrib.staticfiles.finders.FileSystemFinder",
  "django.contrib.staticfiles.finders.AppDirectoriesFinder",
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
)

TEMPLATE_CONTEXT_PROCESSORS = (
  "django.contrib.auth.context_processors.auth",
  "django.core.context_processors.i18n",
  "django.core.context_processors.request",
  "django.core.context_processors.media",
  "django.core.context_processors.static",
)

ROOT_URLCONF = "schedule.urls"

WSGI_APPLICATION = "schedule.wsgi.application"

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
  "mptt",
  "schedule",
  "filer",
  "easy_thumbnails",
  "django.contrib.admin",
  "south",
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

