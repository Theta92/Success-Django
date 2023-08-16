from django.apps import AppConfig


class StudentregConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "studentreg"
    def ready(self):
        import studentreg.signals
