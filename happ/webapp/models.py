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
    shopId = IntegerField( default = 0 )
    name = CharField(max_length =  30 )
    details = CharField( max_length = 30 )
    quantity = IntegerField( default=0)
    cost = IntegerField( default=0)
    image = CharField(max_length =10)

class Shop(models.Model):
    shopId = IntegerField(default=0)
    shopName = CharField(max_length = 30)
    location = CharField(max_length = 30)
    
class Profile(models.Model):
    userId = IntegerField(default=0)
    userName = CharField(max_length = 30)
    user = OneToOneField(User, on_delete=models.CASCADE ,null= True)
    password = CharField(max_length = 30)
    
    
class Order(models.Model):
    userId = IntegerField(default=0)
    orderId = IntegerField(default = 0)
    itemList = ArrayField(CharField(max_length=15))
    quantitiy = ArrayField(CharField(max_length=15))



     