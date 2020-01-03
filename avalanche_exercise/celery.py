import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avalanche_exercise.settings')

app = Celery('avalanche_exercise')

app.conf.broker_url = 'redis://redis:6379/0'

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))