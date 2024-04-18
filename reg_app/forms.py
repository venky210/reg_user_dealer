from django import forms
from reg_app.models import *

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password','user','dealer')
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}
       
       
class ProductCreationForm(forms.ModelForm):
    class Meta:
        model=product
        fields=['pname','qty','price','img','category']


class UpdateCreationForm(forms.ModelForm):
    class Meta:
        model=product
        fields=['pname','qty','price','img','category']



class WishlistForm(forms.ModelForm):
    class Meta:
        model=Wishlist
        fields=[] 



class profileform(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','email']
        help_texts={'username':''}



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']



class UserAddressForm(forms.ModelForm):
    class Meta:
        model =CustomUser
        fields=['username','Address','city','pincode','mobile_no']
        help_texts={'username':''}










# class ShipingAddressForm(forms.ModelForm):
#     class Meta:
#         model=Address
#         fields='__all__'