from django.core.mail import send_mail
from celery_tasks.main import celery_app
from django.conf import settings
from dataVis.dataVis.form import 

@celery_app.task(name='email')
def send_verify_email():
    subject = '邮箱验证'
    html_message = '<p>你好，这是测试<p/>'
    send_mail(subject, '', html_message,
              )
