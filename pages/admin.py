from django.contrib import admin
from django import forms

from products.models import Product, Comment, Images
from categories.models import Category
from shopcart.models import ShopCart
from orders.models import Order, OrderDetail

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

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
admin.site.register(ShopCart)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Images)