import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yibao_demo.settings')

app = Celery('yibao_demo')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
