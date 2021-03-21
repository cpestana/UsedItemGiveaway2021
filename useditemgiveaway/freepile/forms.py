from django import forms 
from .models import Item, Comment

class ItemForm(forms.ModelForm):
    class Meta: 
        model=Items
        fields='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields='__all__'
