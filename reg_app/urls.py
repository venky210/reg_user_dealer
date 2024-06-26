from django.contrib import admin
from django.urls import path
from reg_app.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Registration/',Registration,name='Registration'),
    path('homepage/',homepage,name='homepage'),
    path('loginpage/',loginpage,name='loginpage'),
  
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('create_product/',create_product,name='create_product'),
    path('dealerproductlist/',dealerproductlist,name='dealerproductlist'),
    path('updateproduct/<int:product_id>/',updateproduct,name='updateproduct'),
    path('deleteproduct/<int:product_id>/',deleteproduct,name='deleteproduct'),
    path('addwishlist/<int:product_id>/',addwishlist,name='addwishlist'),
  
    path('wishlist/',wishlist,name='wishlist'),
    path('',allproducts,name='allproducts'),
    path('removewishlistiteam/<int:wishlist_id>/',removewishlistiteam,name='removewishlistiteam'),
    path('product_search/',product_search,name='product_search'),
    path('change_password/',change_password,name='change_password'),
    path('Edit_profile/',Edit_profile,name='Edit_profile'),
   

    path('categories/', category_list, name='category_list'),
    path('categories_deatil/<int:category_id>/', category_detail, name='category_detail'),
    path('categories/create/', add_category, name='category_create'),
    path('categories_update/<int:category_id>/', category_update, name='category_update'),
    path('categories_delete/<int:category_id>/',category_delete, name='category_delete'),

   

    path('lowtohigh/',lowtohigh,name='lowtohigh'),
    path('hightolow/',hightolow,name='hightolow'),

    path('Address/',Address,name='Address'),

    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('checkout/',checkout,name='checkout'),
    path('removecart/<int:cart_item_id>/',removecart, name='removecart'),

    path('update_product_status/<int:product_id>/', update_product_status, name='update_product_status'),
    # path('ShipingAddress/',ShipingAddress,name='ShipingAddress'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)















