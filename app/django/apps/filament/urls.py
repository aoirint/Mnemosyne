"""Mnemosyne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import re_path
from filament import views

app_name = 'filament'
urlpatterns = [
    re_path(r'^filament$', views.index, name='index'),
    re_path(r'^filament/new$', views.new, name='new'),
    re_path(r'^filament/edit/(?P<id>\d+)$', views.edit, name='edit'),
    re_path(r'^filament/info/(?P<id>\d+)$', views.info, name='info'),
]
