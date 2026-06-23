from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Import signals to ensure they are registered when the app is ready
        import api.signals  # noqa: F401
        