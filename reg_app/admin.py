from django.contrib import admin

# Register your models here.
from reg_app.models import *
#from reg_app.forms import CustomUserCreationForm
#from django.contrib.auth.admin import UserAdmin



# class CustomUserAdmin(admin.ModelAdmin):
    
#     list_display=['username','email','user','dealer']
    

admin.site.register(CustomUser)





class ProductAdmin(admin.ModelAdmin):
    list_display=['pk','pname','qty','price']

admin.site.register(product,ProductAdmin)


class WishlistAdmin(admin.ModelAdmin):
    list_display=['pk','user','products','qty']

admin.site.register(Wishlist,WishlistAdmin)


# class CategoryAdmin(admin.ModelAdmin):
#     list_display=['username','category']
admin.site.register(Category)


admin.site.register(Cart)

admin.site.register(CartItem)


# admin.site.register(Address)