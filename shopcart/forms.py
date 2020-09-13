from django.forms import ModelForm
from .models import ShopCart

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']