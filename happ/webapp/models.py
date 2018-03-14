from django.db import models
from django.db.models import (
    CharField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    OneToOneField,
    )
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Item(models.Model):
    itemId = CharField( max_length = 30 )
    shopId = CharField(max_length = 10, default = 'None')
    name = CharField(max_length =  30 )
    details = CharField( max_length = 30 )
    quantity = IntegerField( default=0)
    cost = IntegerField( default=0)
    image = CharField(max_length =10, blank = True)

class Shop(models.Model):
    shopId = CharField(max_length = 10, default = 'None')
    shopName = CharField(max_length = 30,default ="ShopName")
    shopOwner = CharField(max_length = 30, default= "OwnerName")
    shopContact = CharField(max_length = 30, default= "99999")
    location = CharField(max_length = 30)
    
class Profile(models.Model):
    userId = CharField(max_length = 10, default = 'UserId')
    userName = CharField(max_length = 30)
    user = OneToOneField(User, on_delete=models.CASCADE ,null= True)
    password = CharField(max_length = 30)
    
    
class Order(models.Model):
    userId = CharField(max_length = 10, default = 'UserId')
    status = CharField(max_length = 10, default ='waiting')
    shopId = CharField(max_length = 10, default = 'None')
    orderId = IntegerField(default = 0)
    itemList = ArrayField(CharField(max_length=15))
    quantitiy = ArrayField(CharField(max_length=15))



     