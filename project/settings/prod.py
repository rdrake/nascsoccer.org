from .common import *

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [".nascsoccer.org", "192.95.26.56", "ks397485.ip-192-95-26.net"]

SECRET_KEY = os.getenv("SITE_SECRET_KEY", "")

COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter",
]

COMPRESS_STORAGE = "compressor.storage.GzipCompressorFileStorage"
