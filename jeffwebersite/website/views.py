from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from website.models import Product, Category


def homepage(request, pk=None):
    if pk:
        category = Category.objects.get(pk=pk)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'homepage.html', context)


def blockswivels(request):
    context = {
        'name':'Blocks & Swivels',
    }
    return render(request, 'blockswivels.html', context)


def product(request, pk):
    current_product = Product.objects.get(pk=pk)
    context = {
         'product': current_product,
    }
    return render(request, 'product.html', context)


def product1(request):
    context = {
    }
    return render(request, 'product1.html', context)


def product2(request):
    context = {
    }
    return render(request, 'product2.html', context)


def product3(request):
    context = {
    }
    return render(request, 'product3.html', context)

def product4(request):
    context = {
    }
    return render(request, 'product4.html', context)


def product5(request):
    context = {
    }
    return render(request, 'product5.html', context)


def product6(request):
    context = {
    }
    return render(request, 'product6.html', context)


def bopaccumulatorswellcontrol(request):
    context = {
        'name':'BOP-Accumulators-Well Control',
    }
    return render(request, 'bopaccumulatorswellcontrol.html',context)


def casingtubingrunning(request):
    context = {
        'name':'Casing Tubing Running',
    }
    return render(request, 'casingtubingrunning.html',context)

def cementing(request):
    context = {
        'name':'Blocks & Swivels',
    }
    return render(request, 'cementing.html',context)

