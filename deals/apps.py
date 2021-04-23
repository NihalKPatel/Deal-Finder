from django.apps import AppConfig


class DealsConfig(AppConfig):
    name = 'deals'

    def ready(self):
        import deals.signals