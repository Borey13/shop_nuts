from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['name', 'price']
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
