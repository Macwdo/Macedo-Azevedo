from django.apps import AppConfig


class ProcessoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'processo'


    def ready(self, *args, **kwargs) -> None:
        import processo.signals
        super_ready = super().ready(*args, **kwargs)
        return super_ready