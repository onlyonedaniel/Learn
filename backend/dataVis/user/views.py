import logging
from django.http import JsonResponse
from django.views import View
from .form import RegisterForm
import user.logic.logic as user_logic
import user.dao.UserDao as user_dao
from user.models import User
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django_redis import get_redis_connection
logger = logging.getLogger("django")
# Create your views here.


class Register(View):
    def get(self, _request):
        register_form = RegisterForm.__dict__
        logging.info(register_form)
        return JsonResponse(register_form)

    def post(self, _request):
        uuid = _request.POST.get('uuid')
        username = _request.POST.get('username')
        password = _request.POST.get('password')
        mobile = _request.POST.get('mobile')
        varify_code = _request.POST.get('varify_code')
        redis_handle = get_redis_connection('varify_code')
        if user_dao.has_register(username, mobile):
            return JsonResponse({
                "errorcode": -1,
                "data": [],
                "type": "error",
                'message': '用户已经存在，请登陆'
            })
        logger.info(uuid)
        code = redis_handle.get('image_{}'.format(uuid))
        logger.info(str(code))
        if (code is not None) and code.decode('utf8').lower() != varify_code.lower():
            return JsonResponse({
                "errorcode": -1,
                "data": [],
                "type": "error",
                'message': '验证码错误'
            })
        user = user_dao.registe(username, password, mobile)
        logger.info(user)
        login(_request, user)
        return JsonResponse({
            "errorcode": 0,
            "data": [],
            "type": "success",
            'message': "成功注册"
        })


class Login(View):
    def post(self, _request):
        username = _request.POST.get('username')
        password = _request.POST.get('password')
        records = User.objects.filter(username=username, password=password)
        user = authenticate(username=username, password=password)
        
        # _request.META['SameSite'] = 'none'
        login(_request, records[0])
        return JsonResponse({
            "errorcode": 0,
            "data": [],
            "type": "success",
            'message': "成功登陆"
        })
        # 
