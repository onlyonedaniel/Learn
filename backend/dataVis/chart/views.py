import numpy as np
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import chart.dao.dataDao as dataDao
# Create your views here.
from django.conf import global_settings
from dataVis.form import ChartConfig


class ChartOneView(View):
    def get(self, _request):
        random_data = np.random.randint(ChartConfig.low_value,
                                        ChartConfig.max_value, size=ChartConfig.num)
        data = random_data.tolist()
        dataDao.save_chart_one(data)
        return JsonResponse({
            "errorcode": 0,
            "data": data,
            "msg": "success"
        })


class ChartTwoView(View):
    def get(self, _request):
        start = _request.GET.get('start', ChartConfig.start)
        limit = _request.GET.get('limit', ChartConfig.limit)
        data = dataDao.get_chart_two(start=start, limit=limit)
        return JsonResponse({
            "errorcode": 0,
            "data": data,
            "msg": "success"
        })

    def post(self, _request):
        data = _request.POST.get('data')
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
