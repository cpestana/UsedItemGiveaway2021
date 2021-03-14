from django.urls import path
from . import views


urlpatterns = [
path('', views.index, name='index'), 
path('Items/', views.Items, name='Item'), 
path('Comments/', views.Comments, name='Comment'), 

]

