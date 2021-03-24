from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic import DetailView, View
from .models import BlocksSwivels, BopAccumulatorsWellControl, CasingTubingRunning, Cementing, CoilTubing, Compressor, DrillString, DrillingRig, EnginesGensetsSCR, FishingTool, Flowback, Frac, HandlingTool, Manifold, Miscellaneou, MudPumpsConditioning, Nitrogen, OCTG, Offshore, Pumps, Slickline, Snubbing, Subsea, TopDrive, ThruTubing, WellServiceWorkover, WellTest, Wireline, Category, LatestProducts
from .mixins import CategoryDetailMixin


class BaseView (View):

    def get (self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        products = LatestProducts.objects.get_products_for_main_page('blocksswivels', 'octg', 'welltest', 'wireline', 'wellserviceworkover', 'thrutubing', 'subsea', 'snubbing', 'pumps', 'slickline', 'offshore', 'mudpumpsconditioning', 'nitrogen', 'manifold', 'miscellaneou', 'handlingtool', 'fishingtool', 'flowback', 'bopaccumulatorswellcontrol', 'enginesgensetsscr', 'casingtubingrunning', 'cementing', 'drillingrig', 'drillstring', 'frac', 'coiltubing', 'compressor', 'topdrive',)
        context = {
            'categories': categories,
            'products': products
        }
        return render(request, 'base.html', context)


# def test_view(request):
#     categories = Category.objects.get_categories_for_left_sidebar()
#     return render(request, 'base.html', {'categories': categories})


class ProductDetailView(CategoryDetailMixin, DetailView):

    CT_MODEL_MODEL_CLASS = {
        'blocksswivels': BlocksSwivels,
        'bopaccumulatorswellcontrol': BopAccumulatorsWellControl,
        'casingtubingrunning': CasingTubingRunning,
        'cementing': Cementing,
        'coiltubing': CoilTubing,
        'compressor': Compressor,
        'drillstring': DrillString,
        'drillingrig': DrillingRig,
        'enginesgensetsscr': EnginesGensetsSCR,
        'fishingtool': FishingTool,
        'flowback': Flowback,
        'frac': Frac,
        'handlingtool': HandlingTool,
        'manifold': Manifold,
        'miscellaneou': Miscellaneou,
        'mudpumpsconditioning': MudPumpsConditioning,
        'nitrogen': Nitrogen,
        'octg': OCTG,
        'offshore': Offshore,
        'pumps': Pumps,
        'slickline': Slickline,
        'snubbing': Snubbing,
        'subsea': Subsea,
        'topdrive': TopDrive,
        'thrutubing': ThruTubing,
        'wellserviceworkover': WellServiceWorkover,
        'welltest': WellTest,
        'wireline': Wireline

    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'


class CategoryDetailView(CategoryDetailMixin, DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'