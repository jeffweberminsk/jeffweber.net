from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Category
# Create your views here.


class List(TemplateView):
    template_name = 'homepage.html'
    def get(self, request):
        all_categories = Category.objects.all()
        ctx = {
            'all_categories':all_categories,
        }
        return render(request, self.template_name,ctx)




def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)




