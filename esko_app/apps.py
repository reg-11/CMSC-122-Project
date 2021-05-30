from django.apps import AppConfig


class EskoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'esko_app'

    def ready(self):
    	import esko_app.signals
