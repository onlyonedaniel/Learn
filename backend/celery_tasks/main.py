from celery import Celery
import sys
import os
sys.path.append(os.path.abspath('..'))
celery_app = Celery('dataVis')
# 加载配置

celery_app.config_from_object('celery_tasks.config')

celery_app.autodiscover_tasks(['celery_tasks.sms.task'])
