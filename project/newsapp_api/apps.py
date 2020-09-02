from django.apps import AppConfig


class NewsappApiConfig(AppConfig):
    name = 'newsapp_api'

    def ready(self):
        import newsapp_api.signals
