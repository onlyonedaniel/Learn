import numpy as np
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import chart.dao.dataDao as dataDao
# Create your views here.
from django.conf import global_settings
from dataVis.form import ChartConfig
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import logging

logger = logging.getLogger("django")


class ChartOneView(View):
    @method_decorator(login_required)
    def get(self, _request):
        random_data = np.random.randint(ChartConfig.low_value,
                                        ChartConfig.max_value, size=ChartConfig.num)
        data = random_data.tolist()
        dataDao.save_chart_one(data)
        logger.info('get chart ')
        return JsonResponse({
            "errorcode": 0,
            "data": data,
            "msg": "success"
        })


class ChartTwoView(View):
    @method_decorator(login_required)
    def get(self, _request):
        start = _request.GET.get('start', ChartConfig.start)
        limit = _request.GET.get('limit', ChartConfig.limit)
        data = dataDao.get_chart_two(start=start, limit=limit)
        return JsonResponse({
            "errorcode": 0,
            "data": data,
            "msg": "success"
        })

    @method_decorator(login_required)
    def post(self, _request):
        data = _request.POST.get('data')
        print(_request.session.keys())
        if data:
            dataDao.save_chart_two(data)
            return JsonResponse({
                "errorcode": 0,
                "msg": 'success'
            })
        return JsonResponse({
            "errorcode": 1,
            "msg": 'fail'
        })
