from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns = [
path('', views.index, name='index'), 
path('Item/', views.Item, name='Item'), 
path('Comment/', views.Comment, name='Comment'), 
path('newitem/', views.newitem, name='newitem'),
path('newcomment/', views.newcomment, name='newcomment'),
path('accounts/', include('django.contrib.auth.urls')), 
path('loginmessage/', views.loginmessage, name='loginmessage'), 
path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]

