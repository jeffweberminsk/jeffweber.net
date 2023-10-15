from . import views
from django.urls import path

urlpatterns = [
    path('homepage/', views.homepage),
    path('blockswivels/', views.blockswivels),
    path('product/', views.product),
    path('product1/', views.product1),
    path('product2/', views.product2),
    path('product3/', views.product3),
    path('product4/', views.product4),
    path('product5/', views.product5),
    path('product6/', views.product6),
    path('bopaccumulatorswellcontrol/', views.bopaccumulatorswellcontrol),
    path('casingtubingrunning/', views.casingtubingrunning),
    path('cementing/', views.cementing),
    # path('coiltubing/', views.coiltubing),
    # path('compressors/', views.compressors),
    # path('drillstring/', views.drillstring),
]
