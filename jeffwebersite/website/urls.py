from . import views
from django.urls import path

urlpatterns = [
    path('<int:pk>', views.homepage, name='categories_view'),
    path('', views.homepage, name='categories_view'),
    path('product/<int:pk>', views.product, name='product_view'),
]
