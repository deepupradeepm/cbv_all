"""createndupdatecbv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DeleteView
from app61.models import Emp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',CreateView.as_view(model=Emp,template_name="index.html",fields=('idno','name','sal'),success_url='/home/')),
    path('home/',ListView.as_view(model=Emp,template_name="home.html"),name='home'),
    path('update <int:pk>/',UpdateView.as_view(model=Emp,template_name="update.html",fields=('idno','name','sal'),success_url='/home/')),
    path('delete <int:pk>/',DeleteView.as_view(model=Emp,template_name="delete.html",success_url='/home/'))
]
