from django.apps import AppConfig


class NoteConfig(AppConfig):
    default = False
    default_auto_field = "django.db.models.BigAutoField"
    name = "note"
