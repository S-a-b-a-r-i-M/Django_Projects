# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject_task1.settings')

app = Celery('myProject_task1')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.task(bind=True)
def send_message(self, message):
    print(f"Pushed message: {message}")
    print("Done")
