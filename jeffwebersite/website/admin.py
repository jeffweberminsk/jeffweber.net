from django.contrib import admin
from .models import *


# class BlockSwivelsAdminForm(ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['image'].help_text = 'Download images at minimum resolution {}x{}'.format(
#             *Product.MIN_RESOLUTION
#         )
#
#     def clean_image(self):
#         image = self.cleaned_data['image']
#         img = Image.open(image)
#         min_height, min_width = Product.MIN_RESOLUTION
#         if img.height < min_height or img.width < min_width:
#             raise ValidationError('Image resolution is less than minimum!')
#         return image
#
#
# class BlockSwivelsAdmin(admin.ModelAdmin):
#     form = BlockSwivelsAdminForm


admin.site.register(Category)
admin.site.register(BlocksSwivels)
admin.site.register(BopAccumulatorsWellControl)
admin.site.register(CasingTubingRunning)
admin.site.register(Cementing)
admin.site.register(CoilTubing)
admin.site.register(Compressor)
admin.site.register(DrillString)
admin.site.register(DrillingRig)
admin.site.register(EnginesGensetsSCR)
admin.site.register(FishingTool)
admin.site.register(Flowback)
admin.site.register(Frac)
admin.site.register(HandlingTool)
admin.site.register(Manifold)
admin.site.register(Miscellaneou)
admin.site.register(MudPumpsConditioning)
admin.site.register(Nitrogen)
admin.site.register(OCTG)
admin.site.register(Offshore)
admin.site.register(Pumps)
admin.site.register(Slickline)
admin.site.register(Snubbing)
admin.site.register(Subsea)
admin.site.register(TopDrive)
admin.site.register(ThruTubing)
admin.site.register(WellServiceWorkover)
admin.site.register(WellTest)
admin.site.register(Wireline)

