import os

from celery import Celery, platforms
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "fuadmin.settings")

# app = Celery(f"application")
app = Celery(f"system")

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# app.autodiscover_tasks()
platforms.C_FORCE_ROOT = True
