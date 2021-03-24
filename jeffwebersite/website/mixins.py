from django.views.generic.detail import SingleObjectMixin
from .models import Category, BlocksSwivels, BopAccumulatorsWellControl, CasingTubingRunning, Cementing, CoilTubing, Compressor, DrillString, DrillingRig, EnginesGensetsSCR, FishingTool, Flowback, Frac, HandlingTool, Manifold, Miscellaneou, MudPumpsConditioning, Nitrogen, OCTG, Offshore, Pumps, Slickline, Snubbing, Subsea, TopDrive, ThruTubing, WellServiceWorkover, WellTest, Wireline


class CategoryDetailMixin(SingleObjectMixin):

    CATEGORY_SLUG2PRODUCT_MODEL = {

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

    def get_context_data(self, **kwargs):
        if isinstance(self.get_object(), Category):
            model = self.CATEGORY_SLUG2PRODUCT_MODEL[self.get_object().slug]
            context = super().get_context_data(**kwargs)
            context['categories'] = Category.objects.get_categories_for_left_sidebar()
            context['category_products'] = model.objects.all()
            return context
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.get_categories_for_left_sidebar()
        return context
