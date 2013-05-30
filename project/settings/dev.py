from .common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = "6326w8mm=*4yd_+)*jco3l#xq0ry1a#cy3&h&q=73s%p411&!j"

MIDDLEWARE_CLASSES += (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)

INSTALLED_APPS += (
    "debug_toolbar",
    "template_timings_panel",
)

INTERNAL_IPS = ("127.0.0.1",)

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False
}

DEBUG_TOOLBAR_PANELS = (
    "debug_toolbar.panels.version.VersionDebugPanel",
    "debug_toolbar.panels.timer.TimerDebugPanel",
    "debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel",
    "debug_toolbar.panels.headers.HeaderDebugPanel",
    "debug_toolbar.panels.request_vars.RequestVarsDebugPanel",
    "debug_toolbar.panels.template.TemplateDebugPanel",
    "debug_toolbar.panels.sql.SQLDebugPanel",
    "debug_toolbar.panels.signals.SignalDebugPanel",
    "debug_toolbar.panels.logger.LoggingPanel",
    "haystack.panels.HaystackDebugPanel",
    "template_timings_panel.panels.TemplateTimings.TemplateTimings",
)
