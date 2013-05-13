from .common import *

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [".nascsoccer.org", ".rdrake.org"]

SECRET_KEY = os.getenv("SITE_SECRET_KEY", "")

#COMPRESS_CSS_FILTERS = [
#    "compressor.filters.css_default.CssAbsoluteFilter",
#    "compressor.filters.cssmin.CSSMinFilter",
#]
#
#COMPRESS_STORAGE = (
#    "compressor.storage.CompressorFileStorage",
#    "compressor.storage.GzipCompressorFileStorage",
#)
