from django.apps import AppConfig


class DjuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djuser'

    def ready(self):
        import djuser.signals