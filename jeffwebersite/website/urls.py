from django.urls import path
from . import views

# app_name = 'jeffweber'
urlpatterns = [
    path('', views.base, name='base'),
    path('<category_slug>/', views.base, name='category_detail'),
    # path('<product_id>/<slug>/', views.product_detail, name='product_detail')
]
