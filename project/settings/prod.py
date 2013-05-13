from .common import *

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [".nascsoccer.org", ".rdrake.org"]

SECRET_KEY = os.getenv("SITE_SECRET_KEY", "")
