from django.db import models


class Category (models.Model):
    name = models.CharField(max_length=55, verbose_name='category name')

    def __str__(self):
        return self.name


class Product (models.Model):

    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(verbose_name='Image')
    condition = models.CharField(max_length=50, verbose_name='Condition')
    quantity = models.IntegerField(verbose_name='Quantity product')
    location = models.CharField(max_length=50)
    data_posted = models.DateField(auto_now=False, verbose_name='Date')
    price = models.CharField(max_length=50, verbose_name='Price')
    description = models.TextField(verbose_name='Description', null=True)

    def __str__(self):
        return self.title
