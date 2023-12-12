import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery beat Settings

# app.conf.beat_schedule = {
#     'search-new-lawsuits-changes': {
#         'task': 'processo.tasks.search_new_lawsuits_changes',
#         'schedule': crontab(hour=12),
#         'args': ()
#     },
# }

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
