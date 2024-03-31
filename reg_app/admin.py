from django.contrib import admin

# Register your models here.
from reg_app.models import *
from reg_app.forms import *
from django.contrib.auth.admin import UserAdmin


class CustomAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    list_display=['username','email','user','dealer']



admin.site.register(CustomUser,CustomAdmin)





