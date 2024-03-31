from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('user', 'User'),
        ('dealer','Dealer'),
       
       
    )
    role = models.CharField(max_length=100, choices=USER_ROLES)
    user=models.BooleanField(default=False)
    dealer=models.BooleanField(default=False)
   
    
