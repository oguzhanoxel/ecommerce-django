from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User
from products.models import Product, Comment
from categories.models import Category
from products.forms import CommentForm
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

@login_required(login_url="login")
def add_comment_to_product(request, id):
    user = request.user
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.product = product
            comment.approve()
            comment.save()
            return redirect('product_detail', product_id=product.pk)
    else:
        form = CommentForm()
    template = 'products/add_comment_to_product.html'
    context ={
        'form':form,
    }
    return render(request, template, context)

@login_required
def comment_approve(request, id):
    return None
    # comment = get_object_or_404(Comment, pk=id)
    # comment.approve()
    # return redirect('product_detail', product_id=comment.product.pk)

@login_required
def comment_remove(request, id):
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()
    return redirect('comment_list')

@login_required
def comment_list_view(request):
    current_user = request.user
    comments = Comment.objects.filter(user = current_user)
    context = {
        'comments': comments,
    }
    template = 'products/comment_list.html'
    return render(request, template, context)