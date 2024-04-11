from django.contrib import admin
from django.urls import path
from reg_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Registration/',Registration,name='Registration'),
    path('',homepage,name='homepage'),
    path('loginpage/',loginpage,name='loginpage'),
  
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('create_product/',create_product,name='create_product'),
    path('dealerproductlist/',dealerproductlist,name='dealerproductlist'),
    path('updateproduct/',updateproduct,name='updateproduct'),
    path('deleteproduct/<int:product_id>/',deleteproduct,name='deleteproduct'),
    path('addwishlist/<int:product_id>/',addwishlist,name='addwishlist'),
  
    path('wishlist/',wishlist,name='wishlist'),
    path('allproducts/',allproducts,name='allproducts'),
    path('removewishlistiteam/<int:wishlist_id>/',removewishlistiteam,name='removewishlistiteam'),
    path('product_search/',product_search,name='product_search'),
    path('change_password/',change_password,name='change_password'),
    path('profile_edit/',profile_edit,name='profile_edit'),
]
