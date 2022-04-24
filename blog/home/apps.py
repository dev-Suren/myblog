from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        import home.signals


class UserConfig(AppConfig):
    name = 'users'

    def ready(self):
        import home.signals
