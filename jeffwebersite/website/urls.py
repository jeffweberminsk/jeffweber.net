from django.urls import path
from .views import Base


urlpatterns = [
    path('', Base.as_view(), name='base'),
    # path('products/<str:ct_model>', ProductDetailView.as_view(), name='product_detail')
    # path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail')
]
