from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
    template = "orders/orderproduct.html"
    return render(request, template, {})