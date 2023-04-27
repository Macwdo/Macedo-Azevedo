import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery beat Settings

app.conf.beat_schedule = {
    'search-process-alterations': {
        'task': 'processo.tasks.search_process_alterations',
        'schedule': crontab(hour=1),
        'args': ()
    },
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
