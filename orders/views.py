from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from shopcart.models import ShopCart
from orders.models import Order
from orders.models import OrderDetail
from orders.forms import OrderForm
# Create your views here.

@login_required(login_url="login")
def order_list(request):
    template = "orders/order_list.html"
    return render(request, template, {})

@login_required(login_url="login")
def order_detail(request, id):
    template = "orders/order_detail.html"
    return render(request, template, {})

@login_required(login_url="login")
def orderproduct(request):
    current_user = request.user
    form = OrderForm(request.POST or None)
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    total = 0
    numItems = 0
    subtotal = []
    for item in shopcart:
        numItems += 1
        total += item.quantity * item.product.price
    for item in shopcart:
        subtotal.append(item.quantity * item.product.price)
    if request.method == 'POST':
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.save()
 
            for item in shopcart:
                detail = OrderDetail()
                detail.order_id = data.id
                detail.user_id = current_user.id
                detail.product_id = item.product_id
                detail.quantity = item.quantity
                detail.price = item.product.price
                detail.total = item.amount
                detail.save()
            ShopCart.objects.filter(user_id=current_user.id).delete()
            return HttpResponseRedirect(reverse("orderproduct", args=None))
    context = {
        'total': total,
        'numItems': numItems,
        'shopcart': shopcart,
        'subtotal': subtotal,
        'form': form,
    }
    template = "orders/orderproduct.html"
    return render(request, template, context)