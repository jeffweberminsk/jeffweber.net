from django.urls import path
from .views import Base


urlpatterns = [
    path('', Base.as_view(), name='base'),
    # path('products/<str:all_category>/<str:title>/', ProductDetailView.as_view(), name='product_detail')
    # path('category/<str:name>/', CategoryDetailView.as_view(), name='category_detail')
]
