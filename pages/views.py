from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User
from products.models import Product, Comment, Images
from categories.models import Category
from shopcart.models import ShopCart
from products.forms import CommentForm, SearchForm
# Create your views here.

def home_page_view(request):
    categories = Category.objects.all()
    context = {
        'n': range(3),#loop range
        'categories': categories,
    }
    template = "home_page.html"
    return render(request, template, context)

def about_view(request):
    template = "about_page.html"
    return render(request, template, {})

def contact_view(request):
    template = "contact_page.html"
    return render(request, template, {})

def category_view(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category.pk)

    page = request.GET.get('page',1)
    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'n': range(3),#loop range
        'categories': categories,
        'products': products,
    }
    template = "products/category.html"
    return render(request, template, context)

def product_detail_view(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    categories = Category.objects.all()
    images = Images.objects.filter(product=product)
    print(images)
    context = {
        'product': product,
        'categories':categories,
        'images':images,
        'n': range(images.count()),
    }
    template = "products/product_detail.html"
    return render(request, template, context)

def product_search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            categories = Category.objects.all()
            search_query = form.cleaned_data['search_query']
            products = Product.objects.filter(name__icontains=search_query)
            context = {
                'categories': categories,
                'products': products,
            }
            template = "products/products_search.html"
            return render(request, template, context)

@login_required(login_url="login")
def add_comment_to_product(request, id):
    user = request.user
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.product = product
            comment.approve()
            comment.save()
            return redirect('product_detail', slug=product.slug)
    else:
        form = CommentForm()
    request.session['comments_counter'] = Comment.objects.filter(user_id=user.id).count()
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
    user = request.user
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()
    request.session['comments_counter'] = Comment.objects.filter(user_id=user.id).count()
    return redirect('comment_list')

@login_required
def comment_list_view(request):
    current_user = request.user
    comments = Comment.objects.filter(user = current_user)
    request.session['comments_counter'] = Comment.objects.filter(user_id=current_user.id).count()
    context = {
        'comments': comments,
    }
    template = 'products/comment_list.html'
    return render(request, template, context)