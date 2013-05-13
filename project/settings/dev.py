from .common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

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
