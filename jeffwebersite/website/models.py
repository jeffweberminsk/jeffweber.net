from django.db import models
from django.contrib.contenttypes.models import ContentType
# Create your models here.
#Category
#Product
#Order
#Description


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        return products


class LatestProducts:
    objects = LatestProductsManager()


class Category (models.Model):
    name = models.CharField(max_length=1000, verbose_name='category name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product (models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, verbose_name='Title')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Image')
    condition = models.CharField(max_length=50, verbose_name='Condition')
    quantity = models.IntegerField(verbose_name='Quantity product')
    location = models.TextField(max_length=100)
    data_posted = models.DateField(auto_now=False, verbose_name='Date')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')
    description = models.TextField(verbose_name='Description', null=True)

    def __str__(self):
        return self.title


class BlockSwivels(Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class BopAccumulatorsWellControl(Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class CasingTubingRunning (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class Cementing(Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class CoilTubing (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class Compressor (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class DrillString (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class DrillingRig (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class EnginesGensetsSCR (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class FishingTool (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class Flowback (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class Frac (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class HandlingTool (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class Manifold (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class Miscellaneou (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class MudPumpsConditioning (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class Nitrogen (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class OCTG (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class Offshore (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class Pumps (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class Slickline (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class Snubbing (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class Subsea (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class TopDrive (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class ThruTubing (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class WellServiceWorkover (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class WellTest (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)


class Wireline (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)



