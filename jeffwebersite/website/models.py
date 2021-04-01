from django.db import models
from django.urls import reverse


class Category (models.Model):

    name = models.CharField(max_length=55)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product (models.Model):

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(verbose_name='Image')
    condition = models.CharField(max_length=50, verbose_name='Condition')
    quantity = models.IntegerField(verbose_name='Quantity product')
    location = models.CharField(max_length=50)
    data_posted = models.DateField(auto_now=False, verbose_name='Date')
    price = models.CharField(max_length=50, verbose_name='Price')
    description = models.TextField(verbose_name='Description', null=True)
    html_description = models.TextField(verbose_name='HTML Description', null=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])