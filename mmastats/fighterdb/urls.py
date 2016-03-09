from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'addfighter/$', views.add_fighter),
]