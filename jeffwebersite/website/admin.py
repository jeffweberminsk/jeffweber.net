from django.contrib import admin
from . import models


admin.site.register(models.Product)



class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Category._meta.fields]
    search_fields = [field.name for field in models.Category._meta.fields]
    list_filter = ['name']
    class Meta:
        model = models.Category




admin.site.register(models.Category,CategoryAdmin)