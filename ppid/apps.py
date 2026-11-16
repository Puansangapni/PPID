from django.apps import AppConfig


class PpidConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ppid'

    def ready(self):
        import ppid.signal
