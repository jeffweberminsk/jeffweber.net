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


class CategoryDetailView(DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'name'