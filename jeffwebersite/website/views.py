from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Product, Category


class Base(TemplateView):
    template_name = 'base.html'

    def get(self, request):
        all_category = Category.objects.all()
        all_product = Product.objects.all()
        ctx = {
            'all_category': all_category,
            'all_product': all_product

        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        query = request.POST['search']
        result_list = Product.objects.filter(id=query)
        if result_list.count() != 0:
            context = {
              'result_list': result_list,
              'query': query,
            }
        else:
            context = {
                'empty': 'Ничего не найдено',
                'query': query
            }
        return render(request, 'search.html', context)


# class ProductDetailView(DetailView):
#
#     def dispatch(self, request, *args, **kwargs):
#         self.model = self.all_category[kwargs['all_category']]
#         self.queryset = self.model._base_manager.all()
#         return super().dispatch(request, *args, **kwargs)
#
#
#     context_object_name = 'product'
#     template_name = 'product_detail'
#     slug_url_kwarg = 'title'
