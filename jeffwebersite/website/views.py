from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import Product, Category


def base(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'base.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


# def product_detail(request, product_slug=None):
#     product = None
#     products = Product.objects.all()
#     if product_slug:
#         product = get_object_or_404(Product, slug=product_slug)
#         products = products.filter(product=product)
#     return render(request, 'product_detail',
#                   {'product': product,
#                    'products': products})







# class Base(TemplateView):
#     template_name = 'base.html'
#
#     def get(self, request):
#         all_category = Category.objects.all()
#         all_product = Product.objects.all()
#         ctx = {
#             'all_category': all_category,
#             'all_product': all_product
#
#         }
#         return render(request, self.template_name, ctx)
#
#     def post(self, request):
#         query = request.POST['search']
#         result_list = Product.objects.filter(category__name=query)
#         if result_list.count() != 0:
#             context = {
#               'result_list': result_list,
#               'query': query,
#             }
#         else:
#             context = {
#                 'empty': 'Ничего не найдено',
#                 'query': query
#             }
#         return render(request, 'search.html', context)

