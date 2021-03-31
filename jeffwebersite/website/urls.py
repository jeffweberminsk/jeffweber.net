from django.urls import path
from .views import Base, CategoryDetailView


urlpatterns = [
    path('', Base.as_view(), name='base'),
    # path('products/<str:category__name>/<str:title>/', ProductDetailView.as_view(), name='product_detail')
    path('category/<str:name>/', CategoryDetailView.as_view(), name='category_detail')
]
