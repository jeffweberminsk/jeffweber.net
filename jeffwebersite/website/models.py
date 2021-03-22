from PIL import Image
from django.db import models
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.urls import reverse

# Create your models here.
#Category
#Product
#Order
#Description


def get_models_for_count(*model_names):
    return [models.Count(model_name)for model_name in model_names]


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class MinResolutionErrorException(Exception):
    pass


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products


class LatestProducts:
    objects = LatestProductsManager()


class CategoryManager(models.Manager):

    CATEGORY_NAME_COUNT_NAME = {
        'Blocks&Swivels': 'blocksswivels__count',
        'BOP-Accumulators-Well Control': 'bopaccumulatorswellcontrol__count',
        'Casing Tubing Running': 'casingtubingrunning__count',
        'Cementing': 'cementing__count',
        'Coil Tubing': 'coiltubing__count',
        'Compressors': 'compressor__count',
        'Drill String': 'drillstring__count',
        'Drilling Rigs': 'drillingrig__count',
        'Engines-Gensets-SCR': 'enginesgensetsscr__count',
        'Fishing Tools': 'fishingtool__count',
        'Flowback': 'flowback__count',
        'Frac': 'frac__count',
        'Handling Tool': 'handlingtool__count',
        'Manifolds': 'manifold__count',
        'Miscellaneous': 'miscellaneou__count',
        'Mud Pumps-Conditioning': 'mudpumpsconditioning__count',
        'Nitrogen': 'nitrogen__count',
        'OCTG': 'octg__count',
        'Offshore': 'offshore__count',
        'Pumps': 'pumps__count',
        'Slickline': 'slickline__count',
        'Snubbing': 'snubbing__count',
        'Subsea': 'subsea__count',
        'Top Drives': 'topdrive__count',
        'Thru Tubing': 'thrutubing__count',
        'Well Service-Workover': 'wellserviceworkover__count',
        'Well Test': 'welltest__count',
        'Wireline': 'wireline__count',
    }

    def get_queryset(self):
        return super().get_queryset()

    def get_categories_for_left_sidebar(self):
        models = get_models_for_count('blocksswivels', 'bopaccumulatorswellcontrol', 'casingtubingrunning', 'cementing', 'coiltubing', 'compressor', 'drillstring', 'drillingrig', 'enginesgensetsscr', 'fishingtool', 'flowback', 'frac', 'handlingtool', 'manifold', 'miscellaneou', 'mudpumpsconditioning', 'nitrogen', 'octg', 'offshore', 'pumps', 'slickline', 'snubbing', 'subsea', 'thrutubing', 'wellserviceworkover', 'welltest', 'wireline', 'topdrive')
        qs = list(self.get_queryset().annotate(*models))
        data = [
            dict(name=c.name, url=c.get_absolute_url(), count=getattr(c, self.CATEGORY_NAME_COUNT_NAME[c.name]))
            for c in qs
        ]
        return data


class Category (models.Model):
    name = models.CharField(max_length=1000, verbose_name='category name')
    slug = models.SlugField(unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug':self.slug})


class Product (models.Model):

    MIN_RESOLUTION = (400, 400)

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
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Price')
    description = models.TextField(verbose_name='Description', null=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     image = self.image
    #     img = Image.open(image)
    #     min_height, min_width = Product.MIN_RESOLUTION
    #     if img.height < min_height or img.width < min_width:
    #         raise MinResolutionErrorException('Image resolution is less than minimum!')
    #     super().save(*args, **kwargs)


class BlocksSwivels(Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class BopAccumulatorsWellControl(Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class CasingTubingRunning (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Cementing(Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class CoilTubing (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Compressor (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class DrillString (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class DrillingRig (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class EnginesGensetsSCR (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class FishingTool (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Flowback (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Frac (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class HandlingTool (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Manifold (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Miscellaneou (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class MudPumpsConditioning (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Nitrogen (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class OCTG (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Offshore (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Pumps (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Slickline (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Snubbing (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Subsea (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class ThruTubing (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class WellServiceWorkover (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class WellTest (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Wireline (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class TopDrive (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')
