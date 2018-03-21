from django.contrib import admin
from .models import *


class AutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'category', 'price']
    exclude = ["category"]
    list_filter = ('brand', 'model', 'year')

    class Meta:
        model = Auto


admin.site.register(Auto, AutoAdmin)