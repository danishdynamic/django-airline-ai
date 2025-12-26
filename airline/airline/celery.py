import os
from celery import Celery

#Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline.settings')

app = Celery('airline')

#load task modules from all registered Django app configs.

app.config_from_object('django.conf:settings', namespace='CELERY')

# This line will automatically discover tasks.py in each app

app.autodiscover_tasks()

