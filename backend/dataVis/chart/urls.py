from django.urls import path
from chart.views import ChartOneView, ChartTwoView
urlpatterns = [
    path('1/', ChartOneView.as_view(), name='chartOne'),
    path('2/', ChartTwoView.as_view(), name='chartTwo'),
]
