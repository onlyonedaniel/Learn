from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django_redis import get_redis_connection
from varification.utils import get_valid_code_img
import base64
from celery_tasks.sms import task
# Create your views here.
import logging
logger = logging.getLogger("django")


class ImageCodeView(View):
    def get(self, request, uuid):
        """
            :param uuid
        """
        logger.info("123")
        code_str, image = get_valid_code_img()
        logger.info(code_str)
        # logger.info(image)
        redis_cnn = get_redis_connection('varify_code')
        pipline = redis_cnn.pipeline()
        pipline.setex('image_{}'.format(uuid), 300, code_str)
        pipline.execute()
        task.task_test.delay()
        return HttpResponse(base64.b64encode(image), content_type='image/jpg')

    def post(self, request):
        pass
