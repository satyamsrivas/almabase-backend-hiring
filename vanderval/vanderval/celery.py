from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vanderval.settings")

app = Celery('vanderval')

# Load task modules from all registered Django app configs
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in installed apps
app.autodiscover_tasks()