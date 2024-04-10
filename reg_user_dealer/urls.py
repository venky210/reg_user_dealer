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
    path('',Registration,name='Registration'),
    path('homepage/',homepage,name='homepage'),
    path('loginpage/',loginpage,name='loginpage'),
  
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('create_product/',create_product,name='create_product'),
    path('dealerproductlist/',dealerproductlist,name='dealerproductlist'),
    path('updateproduct/',updateproduct,name='updateproduct'),
    path('deleteproduct',deleteproduct,name='deleteproduct'),
    path('addwishlist/',addwishlist,name='addwishlist'),
  
    path('wishlist/',wishlist,name='wishlist'),
    path('allproducts/',allproducts,name='allproducts'),
    path('removewishlistiteam/',removewishlistiteam,name='removewishlistiteam'),
    path('product_search/',product_search,name='product_search'),
    path('change_password/',change_password,name='change_password'),
    path('profile_edit/',profile_edit,name='profile_edit'),
]
