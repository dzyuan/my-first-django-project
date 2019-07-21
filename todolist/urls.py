from django.contrib import admin,auth
from django.contrib.auth import views as auth_views
from django.urls import path,reverse,reverse_lazy
from . import views
from django.conf.urls import url




urlpatterns = [
   
  
    path('',views.projectlist,name='project_list'),
   
    path('delete/<projectid>',views.deleteproject,name='project_delete'),
    path('edit/<projectid>',views.editproject,name='project_edit'),
    path('add',views.addproject.as_view(),name='project_add'),


]
