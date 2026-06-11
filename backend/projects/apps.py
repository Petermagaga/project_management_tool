from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field=(
        "django.models.BigAutoField"
    )
    name = 'projects'

    def ready(self):
        import projects.signals
