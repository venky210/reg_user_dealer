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
        fields=['pname','qty','price','img']


class UpdateCreationForm(forms.ModelForm):
    class Meta:
        model=product
        fields=['pname','qty','price']

class DeleteCreationForm(forms.ModelForm):
    class Mpeta:
        model=product
        fields=['pname']


class WishlistForm(forms.ModelForm):
    class Meta:
        model=Wishlist
        fields=['products','qty'] 
