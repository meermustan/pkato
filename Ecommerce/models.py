from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files import File 
import urllib
# Create your models here.
class Product(models.Model):
    Title = models.CharField(max_length=250)
    Description = models.TextField()
    Category = models.CharField(max_length=150)
    Sub_Category = models.CharField(max_length=150)
    Brand = models.CharField(max_length=150)
    Picture = models.ImageField()
    Picture2 = models.ImageField(blank=True,default="")
    Picture3 = models.ImageField(blank=True,default="")
    Picture4 = models.ImageField(blank=True,default="")
    Price = models.IntegerField()
    Stock = models.IntegerField(default=5)
    Pub_Date = models.DateTimeField(default=timezone.now)
    Choices = models.JSONField(blank=True,default="")
    Questions = models.TextField(blank=True)
    def __str__(self):
        return self.Title

class Intresting_Product(models.Model):
    User = models.CharField(max_length=20)
    Product = models.IntegerField()
    def __str__(self):
        return self.User
    
class Size_Choice(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.choice

class UserDetails(models.Model):
    User = models.CharField(max_length=20)
    Cart = models.JSONField(blank=True,default=0)
    Wish_List = models.JSONField(blank=True,default=0)
    def __str__(self):
        return self.User

class Order(models.Model):
    Item = models.CharField(max_length=20)
    ItemQty = models.IntegerField()
    ItemPrice = models.IntegerField(default=1)
    Email = models.CharField(max_length=100)
    PhoneNumber = models.IntegerField()
    Address = models.TextField()
    Address2 = models.TextField(blank=True)
    Province = models.CharField(max_length=50)
    City = models.CharField(max_length=100)
    ZipPortal = models.IntegerField()
    Details_On_Email = models.BooleanField()
    Pub_Date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "Porduct " + self.Item + " by " + self.Email
    


