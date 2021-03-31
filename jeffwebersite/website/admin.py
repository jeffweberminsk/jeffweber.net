from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

    class Meta:
        model = models.Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'price']
    search_fields = ['title', 'id', 'category__name']

    class Meta:
        model = models.Product


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)