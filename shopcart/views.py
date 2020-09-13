from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def shopcart_list(request):
    template = "shopcart/shopcart.html"
    return render(request, template, {})

@login_required(login_url="login")
def shopcart_add(request, id):
    return None

@login_required(login_url="login")
def shopcart_delete(request, id):
    return None