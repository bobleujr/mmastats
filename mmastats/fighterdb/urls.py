from django.conf.urls import url

from . import views
from . import maclearn

urlpatterns = [
    url(r'addfighter/$', views.add_fighter),
    url(r'updatehashers/$', views.get_updated_hashers),
    url(r'getfightsmetrics/$', views.get_fights_metrics),
    url(r'getfightermetrics/$', views.get_fighter_metrics),
    url(r'case1/$', maclearn.case1),


]