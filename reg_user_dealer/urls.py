"""
URL configuration for reg_user_dealer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from reg_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Registration/',Registration,name='Registration'),
    path('homepage/',homepage,name='homepage'),
    path('loginpage/',loginpage,name='loginpage'),
    path('userdashbord/',userdashbord,name='userdashbord'),
    path('dealerdashbord/',dealerdashbord,name='dealerdashbord'),
    path('logoutpage/',logoutpage,name='logoutpage'),
]
