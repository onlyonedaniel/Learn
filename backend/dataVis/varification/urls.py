from django.urls import path, re_path
from varification.views import ImageCodeView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    re_path(r'^image_code/(?P<uuid>[\w-]+)/$',
            ImageCodeView.as_view(), name='image_code'),
]
