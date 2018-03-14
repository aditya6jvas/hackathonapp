from django.core import serializers
from django.http import Http404, HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from webapp.models import Item, Shop, Profile, Order
from . import gcm
# Create your views here.

def push(request):
    gcm.PushNotification()

@csrf_exempt
def addShop(request):
    if request.method == 'POST':
        shopId = get_random_string(3).lower()
        shopName = request.POST.get('shopName')
        shopOwner = request.POST.get('shopOwner')
        shopContact = request.POST.get('shopContact')
        location = request.POST.get('location')

        shopObj = Shop(shopId = shopId, shopName = shopName, shopOwner = shopOwner, shopContact = shopContact)
        shopObj.save()

        json_data = serializers.serialize('json', [shopObj,])
        return HttpResponse(json_data, content_type="application/json")

    else:
        return HttpResponse('This is an invalid response, try post')

@csrf_exempt
def addItem(request):
    if request.method=='POST':
        ItemId = get_random_string(3).lower()
        shopId = request.POST.get('shopId')
        name = request.POST.get('name')
        details = request.POST.get('details')
        quantity = request.POST.get('quantity')
        cost = request.POST.get('cost')
        
        itemObj = Item(ItemId = ItemId, shopId = shopId, name = name, details = details, quantity = quantity, cost = cost )
        itemObj.save()

        json_data = serializers.serialize('json', itemObj)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse('This is an invalid response, try post')

@csrf_exempt
def viewItems(request):
    if request.method == 'POST':
        shopId = request.POST.get('shopId')
        queryset = Item.objects.filter(shopId = shopId)
        
        json_data = serializers.serialize('json', queryset)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse('This is an invalid response, try post')

@csrf_exempt
def viewOrder(request):
    if request.method == 'POST':

        queryset = Order.objects.filter(shopId = request.POST.get('shopId'))
        json_data = serializers.serialize('json', queryset)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse('This is an invalid response, try post')
    
# def acceptOrder(request):
#     if request.method == 'POST':

        
