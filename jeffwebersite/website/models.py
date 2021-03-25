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
        return reverse('category_detail', kwargs={'slug': self.slug})


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
    location = models.CharField(max_length=50)
    data_posted = models.DateField(auto_now=False, verbose_name='Date')
    price = models.CharField(max_length=50, verbose_name='Price')
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

    def get_listing_id(self):
        return '11'+str(self.id)


class BopAccumulatorsWellControl(Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '12'+str(self.id)


class CasingTubingRunning (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '13'+str(self.id)


class Cementing(Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '14'+str(self.id)


class CoilTubing (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '15'+str(self.id)


class Compressor (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '16'+str(self.id)


class DrillString (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '17'+str(self.id)


class DrillingRig (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '18'+str(self.id)


class EnginesGensetsSCR (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '19'+str(self.id)


class FishingTool (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '20'+str(self.id)


class Flowback (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '21'+str(self.id)


class Frac (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '22'+str(self.id)


class HandlingTool (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '23'+str(self.id)


class Manifold (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '24'+str(self.id)


class Miscellaneou (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '25'+str(self.id)


class MudPumpsConditioning (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '26'+str(self.id)


class Nitrogen (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '27'+str(self.id)


class OCTG (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '28'+str(self.id)


class Offshore (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '29'+str(self.id)


class Pumps (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '30'+str(self.id)


class Slickline (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '31'+str(self.id)


class Snubbing (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '32'+str(self.id)


class Subsea (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '33'+str(self.id)


class ThruTubing (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '34'+str(self.id)


class WellServiceWorkover (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '35'+str(self.id)


class WellTest (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '36'+str(self.id)


class Wireline (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '37'+str(self.id)


class TopDrive (Product):
    def __str__(self):
        return '{}:{}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def get_listing_id(self):
        return '38'+str(self.id)
