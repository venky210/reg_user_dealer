from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('user','User'),
        ('dealer','Dealer'),
       
       
    )
   
    user=models.BooleanField(default=False)
    dealer=models.BooleanField(default=False)
   
    
