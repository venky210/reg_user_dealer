from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('user','User'),
        ('dealer','Dealer'),
        ('admin','Admin'),
        
       
       
    )


    Address=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    pincode=models.IntegerField(blank=True,null=True)
    mobile_no=models.IntegerField(blank=True,null=True)

   
    user=models.BooleanField(default=False)
    dealer=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)


class Category(models.Model):
   
    category=models.CharField(max_length=100,unique=True)


    def __str__(self):
        return self.category





class product(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),)
    
    
    pname=models.CharField(max_length=100)
    qty=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    img=models.ImageField()
    dealer=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.pname


 
class Wishlist(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    products=models.ForeignKey(product,on_delete=models.CASCADE,null=True,blank=True)
  
    qty=models.IntegerField(default=1)

    


    # def __str__(self):
    #     return self.products


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

  
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)















   
# class Address(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     city=models.CharField(max_length=100,blank=True,null=True)
#     mobile_number = models.CharField(max_length=15, blank=True, null=True)
#     current_location = models.CharField(max_length=255, blank=True, null=True)
#     pincode=models.IntegerField(blank=True, null=True)

    # def __str__(self):
    #     return self.user.username