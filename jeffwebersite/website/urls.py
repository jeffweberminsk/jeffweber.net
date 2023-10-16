from . import views
from django.urls import path

urlpatterns = [
    path('homepage/<int:pk>', views.homepage, name='categories_view'),
    path('homepage/', views.homepage, name='categories_view'),
    path('product/<int:pk>', views.product, name='product_view'),
]
