from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand', 'quantity', 'created_at', 'updated_at')
    search_fields = ('title', 'category__name', 'brand__name')


admin.site.register(Product, ProductAdmin)