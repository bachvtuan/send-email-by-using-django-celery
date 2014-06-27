from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os
# Indicate Celery to use the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('proj',
             broker='redis://localhost:6379/0',
             backend='redis://localhost',
             include=['app.tasks'])

app.config_from_object('django.conf:settings')

# Optional configuration, see the application user guide.
app.conf.update(
  CELERY_TASK_RESULT_EXPIRES=3600,
  CELERYD_CONCURRENCY = 2
)

if __name__ == '__main__':
    app.start()