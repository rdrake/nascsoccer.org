from .common import *

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["*"]

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECRET_KEY = os.getenv("SITE_SECRET_KEY", "")

# Cache the templates only in production.
TEMPLATE_LOADERS = (
    ("django.template.loaders.cached.Loader", TEMPLATE_LOADERS),
)

COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter",
]

COMPRESS_STORAGE = "compressor.storage.GzipCompressorFileStorage"
