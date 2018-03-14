from django.contrib import admin
from .models import (Item,
    Shop,
    Profile,
    Order,)
# Register your models here.

admin.site.register(Item)
admin.site.register(Shop)
admin.site.register(Profile)
admin.site.register(Order)