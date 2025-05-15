from django.apps import AppConfig # type: ignore

class CatsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cats'
