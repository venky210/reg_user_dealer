from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('user','User'),
        ('dealer','Dealer'),
        ('admin','Admin'),
        
       
       
    )
   
    user=models.BooleanField(default=False)
    dealer=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)


class Category(models.Model):
   
    category=models.CharField(max_length=100,unique=True)


    def __str__(self):
        return self.category





class product(models.Model):
    
    pname=models.CharField(max_length=100)
    qty=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    img=models.ImageField()
    dealer=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.pname


 
class Wishlist(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    products=models.ForeignKey(product,on_delete=models.CASCADE,null=True,blank=True)
  
    qty=models.IntegerField(default=1)

    


    # def __str__(self):
    #     return self.products



   
   