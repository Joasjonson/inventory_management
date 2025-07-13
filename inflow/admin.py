from django.contrib import admin
from .models import Inflow

class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'description', 'created_at', 'updated_at')
    search_fields = ('supplier__name', 'product__title', 'description')

admin.site.register(Inflow, InflowAdmin)