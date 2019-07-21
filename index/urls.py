from django.contrib import admin,auth
from django.contrib.auth import views as auth_views
from django.urls import path,reverse,reverse_lazy
from . import views
from django.conf.urls import url


app_name = 'index'


urlpatterns = [
   
    path('',views.index,name='index'),
   

]
