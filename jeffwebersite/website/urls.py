from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^homepage/$', views.homepage),


]
#http://127.0.0.1:8000/homepage/