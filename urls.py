"""job URL Configuration

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
from django.contrib import admin
from django.urls import path
from appjob.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path("login/",Login_page,name='Login_page'),
    path('create/',createpage,name='createpage'),
    path('contain/',contain_page,name='contain_page'),
    path('details/<int:e>/',details,name='details'),
    path('logout/',logout_page,name='logout_page'),
    path('search/',search_page,name='search_page'),
    path('login_page/',lpage,name='lpage'),
]
