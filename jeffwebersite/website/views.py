from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import BlocksSwivels, BopAccumulatorsWellControl, CasingTubingRunning, Cementing, CoilTubing, Compressor, DrillString, DrillingRig, EnginesGensetsSCR, FishingTool, Flowback, Frac, HandlingTool, Manifold, Miscellaneou, MudPumpsConditioning, Nitrogen, OCTG, Offshore, Pumps, Slickline, Snubbing, Subsea, TopDrive, ThruTubing, WellServiceWorkover, WellTest, Wireline
# Create your views here.


def test_view(request):
    context = {}
    return render(request, 'base.html', context)


class ProductDetailView(DetailView):

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
        'wireline': Wireline,

    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'

