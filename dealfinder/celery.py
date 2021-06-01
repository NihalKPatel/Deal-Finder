from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dealfinder.settings')
app = Celery('dealfinder')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# execute scheduled task every sunday at midnight
app.conf.beat_schedule = {
    'weekly-budget': {
        'task': 'deals.tasks.create_weekly_budgets',
        'schedule': crontab(hour=0, minute=0, day_of_week=6),
    }
}


