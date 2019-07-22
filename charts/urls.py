from django.conf.urls import url
from .views import get_data, charts, ChartData

urlpatterns = [
    url(r'^$', get_data, name='get_data'),
    url(r'^api/chart/data$', ChartData.as_view()),
    url(r'^charts$', charts, name='charts'),
]