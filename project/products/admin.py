from django.contrib import admin
from .models import *
from django import forms

# Register your models here.


admin.site.register(Brands)
admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(GenderType)
admin.site.register(HashTag)
admin.site.register(Manufacturer)
admin.site.register(TypeModel)
admin.site.register(Size)
admin.site.register(Image)
admin.site.register(NomenSet)
admin.site.register(Characteristics)
admin.site.register(Product)
admin.site.register(Set)


class ColorAdmin(admin.ModelAdmin):
    list_per_page = 100

    search_fields = ['name', 'nameid', 'guid', 'nametwo', 'hexcode']
    filter_horizontal = ('images',)


admin.site.register(Color, ColorAdmin)
