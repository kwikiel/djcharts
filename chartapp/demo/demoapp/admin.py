from django.contrib import admin
from .models import LineModel, DonutModel


class LineAdmin(admin.ModelAdmin):
    list_display = ('xfield', 'yfield')

# Register your models here.
# admin.site.register(LineModel, LineAdmin)
# admin.site.register(DonutModel)
