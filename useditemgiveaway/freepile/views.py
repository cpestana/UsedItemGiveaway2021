from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Items, Comments
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'freepile/index.html')

def getItems(request, id):
    Items_list=get_object_or_404(Items, pk=id)
    return render(request, 'freepile/items.html', {'Items_list': Items_list} )

def getComments(request, id):
    Comments_list=Comments.objects.all()
    return render(request, 'freepile/comments.html', {'Comments_list': Comments_list})