from django import forms 
from .models import Items, Comments 

class ItemForm(forms.ModelForm):
    class Meta: 
        model=Items
        fields='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields='__all__'
