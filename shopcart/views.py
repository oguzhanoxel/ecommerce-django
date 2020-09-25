from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from shopcart.models import ShopCart
from products.models import Product
from shopcart.forms import ShopCartForm

# Create your views here.

@login_required(login_url="login")
def shopcart_list(request):
    quantity = 1
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    subtotal = []
    for item in shopcart:
        total += item.quantity * item.product.price
    for item in shopcart:
        subtotal.append(item.quantity * item.product.price)
    request.session['shopcart_counter'] = ShopCart.objects.filter(user_id=current_user.id).count()
    context = {
        'shopcart': shopcart,
        'subtotal': subtotal,
        'total': total,
    }
    template = "shopcart/shopcart.html"
    return render(request, template, context)

@login_required(login_url="login")
def shopcart_add(request, id):
    url = request.META.get('HTTP_REFERER')
    form = ShopCartForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            current_user = request.user
            quantity = form.cleaned_data['quantity']
            data = ShopCart(user_id=current_user.id, product_id=id, quantity=quantity)
            data.save()
            messages.success(request, "{} add to cart.".format(data.product.name))
            return HttpResponseRedirect(reverse('shopcart_list', args=None))
    current_user = request.user
    quantity = 1
    data = ShopCart(user_id=current_user.id, product_id=id, quantity=quantity)
    data.save()
    messages.success(request, "{} add to cart.".format(data.product.name))
    return HttpResponseRedirect(url)

@login_required(login_url="login")
def shopcart_delete(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.warning(request, "Product deleted from cart.")
    return HttpResponseRedirect(reverse('shopcart_list', args=None))
