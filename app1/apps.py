from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'
    verbose_name = _("app1")
