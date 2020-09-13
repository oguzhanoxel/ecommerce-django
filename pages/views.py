from django.shortcuts import render
from products.models import Product
from categories.models import Category
from django.http import Http404
# Create your views here.

def home_page_view(request):
    categories = Category.objects.all()
    context = {
        'n': range(3),#loop range
        'categories': categories,
    }
    template = "home_page.html"
    return render(request, template, context)

def category_view(request, category_id):
    categories = Category.objects.all()
    products = Product.objects.filter(category=category_id)
    context = {
        'n': range(3),#loop range
        'categories': categories,
        'products': products,
    }
    template = "products/category.html"
    return render(request, template, context)

def product_detail_view(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories':categories,
    }
    template = "products/product_detail.html"
    return render(request, template, context)