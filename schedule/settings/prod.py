from schedule.settings.common import *

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": os.getenv("SITE_DB_NAME", ""),
    "USER": os.getenv("SITE_DB_USER", ""),
    "PASSWORD": os.getenv("SITE_DB_PASSWORD", ""),
    "HOST": "",
    "PORT": "",
  }
}

ALLOWED_HOSTS = [".nascsoccer.org"]

SECRET_KEY = os.getenv("SITE_SECRET_KEY", "")
