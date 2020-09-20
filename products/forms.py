from django.forms import ModelForm
from products.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']