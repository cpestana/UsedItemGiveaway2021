from django.contrib import admin 
from django.urls import path
from . import views
from django.config.urls import include

urlpatters = {
path('', view.index, name='index'), 
path('Items/', views.Items, name='Item'), 
path('Comments/', view.Comments, name='Comment'), 

}

