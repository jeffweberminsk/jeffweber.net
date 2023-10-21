from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from website.models import Product, Category


def homepage(request, pk=None):
    context = {}

    if pk:
        category = Category.objects.get(pk=pk)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    categories = Category.objects.all().order_by('name')

    context['categories'] = categories

    if request.method == 'POST':
        search_term = request.POST.get('search', '')
        print(search_term)

        q_title = Q(product_title__icontains=search_term)
        q_description = Q(description__icontains=search_term)

        q_combined = q_title | q_description
        print(q_combined)
        results = Product.objects.filter(q_combined)

        context['products'] = results

    else:
        context['products'] = products

    print(context['products'])
    return render(request, 'homepage.html', context)



def product(request, pk):
    current_product = Product.objects.get(pk=pk)
    context = {
        'product': current_product,
    }
    products = Product.objects.all()

    categories = Category.objects.all().order_by('name')

    context['categories'] = categories
    return render(request, 'product.html', context)




