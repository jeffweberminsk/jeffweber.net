from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name']
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'price']
    search_fields = ['title', 'id', 'category__name']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)