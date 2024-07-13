# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HemoHubProject.settings')
from celery.schedules import crontab
app = Celery('HemoHubProject')
app.conf.beat_schedule = {
    'check-expiring-blood-products-every-day': {
        'task': 'HemoHubApp.tasks.check_expiring_blood_products',
        'schedule': crontab(hour=0, minute=0),  # Every day at midnight
    },
}
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
