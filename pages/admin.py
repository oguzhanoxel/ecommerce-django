from django.contrib import admin
from django import forms

from products.models import Product
from categories.models import Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'id',
        'category',
        'stock',
        'price',
        'is_active',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'id',
        'parent',
        'is_active',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)