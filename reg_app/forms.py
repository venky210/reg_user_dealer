from django import forms
from reg_app.models import *

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email','password','user','dealer']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}
       
       
