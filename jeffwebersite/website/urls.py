from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^homepage/$', views.homepage),
    url(r'^blockswivels/$',views.blockswivels),
    url(r'^product/$', views.product),
    url(r'^product1/$', views.product1),
    url(r'product2/$', views.product2),
    url(r'product3/$', views.product3),
    url(r'product4/$', views.product4),
    url(r'product5/$', views.product5),
    url(r'product6/$', views.product6),
    url(r'^bopaccumulatorswellcontrol/$',views.bopaccumulatorswellcontrol),
    url(r'^casingtubingrunning/$',views.casingtubingrunning),
    url(r'^cementing/$',views.cementing),
    # url(r'^coiltubing',views.coiltubing),
    # url(r'^compressors',views.compressors),
    # url(r'^drillstring',views.drillstring)

]