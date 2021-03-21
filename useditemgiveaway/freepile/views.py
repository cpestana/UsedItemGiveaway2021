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
    return render(request, 'freepile/Item.html', {'Items_list': Items_list} )

def getComments(request, id):
    Comments_list=Comments.objects.all()
    return render(request, 'freepile/Comment.html', {'Comments_list': Comments_list})

@login_required
def newitem(request):
     form=ItemForm

     if request.method=='POST':
          form=ItemForm(request.POST)

          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ItemForm()
     else:
          form=ItemForm()

     return render(request, 'freepile/newitem.html', {'form': form})

def newcomment(request):
    form=CommentForm

    if request.method=='POST':
        form=CommentForm(request.POST)

        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=CommentForm()
    else: 
        form=CommentForm()

    return render(request, 'freepile/newcomment.html', {'form': form})

def loginmessage(request):
    return render(request, 'freepile/loginmessage.html')

def logoutmessage(request):
    return render(request, 'freepile/logoutmessage.html')

