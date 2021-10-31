# 定义任务
import time
from celery_tasks.main import celery_app


@celery_app.task(name='task_test')
def task_test():
    i = 0
    while i < 10:
        time.sleep(2)
        print('task test')
        i += 1
    return 0
