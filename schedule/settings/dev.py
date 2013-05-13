from schedule.settings.common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.postgresql_psycopg2", # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
    "NAME": "schedule",            # Or path to database file if using sqlite3.
    # The following settings are not used with sqlite3:
    "USER": "",
    "PASSWORD": "",
    "HOST": "127.0.0.1",            # Empty for localhost through domain sockets or "127.0.0.1" for localhost through TCP.
    "PORT": "",            # Set to empty string for default.
  }
}

SECRET_KEY = "6326w8mm=*4yd_+)*jco3l#xq0ry1a#cy3&h&q=73s%p411&!j"

MIDDLEWARE_CLASSES += (
  "debug_toolbar.middleware.DebugToolbarMiddleware",
)

INSTALLED_APPS += (
  "debug_toolbar",
)

INTERNAL_IPS = ("127.0.0.1",)

DEBUG_TOOLBAR_CONFIG = {
  "INTERCEPT_REDIRECTS": False
}
