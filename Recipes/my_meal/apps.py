from django.apps import AppConfig


class MyMealConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_meal'

    def ready(self):
        import my_meal.signals  # Load signals when the app starts