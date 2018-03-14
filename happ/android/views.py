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

        shopObj = Shop(shopId = shopId, shopName = shopName, shopOwner = shopOwner, shopContact = shopContact, location = location)
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
        
        itemObj = Item(itemId = ItemId, shopId = shopId, name = name, details = details, quantity = quantity, cost = cost )
        itemObj.save()

        json_data = serializers.serialize('json', [itemObj,])
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
def singleItem(request):
    if request.method == 'POST':
        shopId = request.POST.get('shopId')
        itemId = request.POST.get('shopId')
        try:
            queryset = Item.objects.get(shopId = shopId, itemId = itemId)
        except Item.DoesNotExist:
            return HttpResponse("Item doesn't")
        
        json_data = serializers.serialize('json', queryset)
        return HttpResponse(json_data, content_type="application/json")

    else:
        return HttpResponse('This is an invalid response, try post')



@csrf_exempt
def editItem(request):
    if request.method == 'POST':
        shopId = request.POST.get('shopId')
        itemId = request.POST.get('itemId')
        name = request.POST.get('name')
        details = request.POST.get('details')
        quantity = request.POST.get('quantity')
        cost = request.POST.get('cost')
        try:
            itemObj = Item.objects.get(itemId = itemId, shopId = shopId)
        except Item.DoesNotExist:
            return HttpResponse("no Obj")
        itemObj.name = name
        itemObj.details = details
        itemObj.quantity = quantity
        itemObj.cost = cost
        itemObj.save()

        return HttpResponse("Success")

    else:
        return HttpResponse('This is an invalid response, try post')

@csrf_exempt
def waitingOrder(request):
    if request.method == 'POST':
        queryset = Order.objects.filter(shopId = request.POST.get('shopId'), status  = 'waiting')
        json_data = serializers.serialize('json', queryset)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse('This is an invalid response, try post')

@csrf_exempt
def confirmedOrder(request):
    if request.method == 'POST':
        queryset = Order.objects.filter(shopId = request.POST.get('shopId'), status = 'confirmed')
        json_data = serializers.serialize('json', queryset)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse('This is an invalid response, try post')

@csrf_exempt
def singleOrder(request):
    if request.method == 'POST':
        queryset = Order.objects.filter(shopId = request.POST.get('shopId'), orderId = request.POST.get('orderId'))
        json_data = serializers.serialize('json', queryset)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse('This is an invalid response, try post')


@csrf_exempt
def killedOrder(request):
    if request.method == 'POST':
        queryset = Order.objects.filter(shopId = request.POST.get('shopId'), status  = 'killed')
        json_data = serializers.serialize('json', queryset)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse('This is an invalid response, try post')


@csrf_exempt
def acceptOrder(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderId')
        status = 'confirmed'

        queryset = Order.objects.filter(orderId = orderId)
        queryset.status = status
        queryset.save()

        json_data = serializers.serialize('json', queryset)
        return HttpResponse(json_data, content_type="application/json")

    else:
        return HttpResponse('This is an invalid response, try post')

@csrf_exempt
def killOrder(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderId')
        status = 'killed'

        try:
            queryset = Order.objects.get(orderId = orderId)
        except Order.DoesNotExist:
            return HttpResponse("No Order found")
        
        queryset.status = status
        items = []
        items = queryset.itemList
        quantity = []
        quantity  = queryset.quantity
        
        for i in range(items.length):
            query = Item.objects.get(itemId = items[i])
            query.quantity -= quantity[i]
            query.save()


        queryset.save()

        json_data = serializers.serialize('json', queryset)
        return HttpResponse(json_data, content_type="application/json")

    else:
        return HttpResponse('This is an invalid response, try post')

        
