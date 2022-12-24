from django.apps import AppConfig


class CounterappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "counterapp"

    def ready(self):
        from counterapp.views import REDIS_KEY
        from counterapp.models import Counter, MySQLCounter
        # Reset counter to 0
        Counter.objects.update_or_create(name=REDIS_KEY, defaults={'count': 0})
        MySQLCounter.objects.update_or_create(name=REDIS_KEY, defaults={'count': 0})

