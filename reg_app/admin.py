from django.contrib import admin

# Register your models here.
from reg_app.models import CustomUser
#from reg_app.forms import CustomUserCreationForm
#from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(admin.ModelAdmin):
    
    list_display=['username','email','user','dealer']
    



admin.site.register(CustomUser,CustomUserAdmin)





