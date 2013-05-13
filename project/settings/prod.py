from .common import *

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [".nascsoccer.org", ".rdrake.org"]

SECRET_KEY = os.getenv("SITE_SECRET_KEY", "")

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "unix:/tmp/memcached.sock",
    }
}

#COMPRESS_CSS_FILTERS = [
#    "compressor.filters.css_default.CssAbsoluteFilter",
#    "compressor.filters.cssmin.CSSMinFilter",
#]
#
#COMPRESS_STORAGE = [
#    "compressor.storage.CompressorFileStorage",
#    "compressor.storage.GzipCompressorFileStorage",
#]
