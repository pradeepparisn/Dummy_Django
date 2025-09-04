from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("apply/",views.apply,name='apply'),
    path("feedback/",views.feedback,name='feedback'),
    #path("appliedcontact/",views.appliedcontact,name='appliedcontact')


]