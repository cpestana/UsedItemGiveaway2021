from .models import Item, Comment
from django import forms

class ItemForm(forms.ModelForm):
    class Meta: 
        model=Item
        fields='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'

