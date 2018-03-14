from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect,HttpResponse
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Shop, Profile, Order, Item
# Create your views here.

def index(request):
	if request.method == 'POST':
		user = request.POST.get('userName')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		print(user)
		print(email)
		print(mobile)
		return HttpResponse('abc')
	else:
		return render(request, 'index.html', {})

def hi(request):
    
    queryset = Shop.objects.all()
    return render(request, 'index1.html', {'queryset':queryset})

def cart(request, shopId):
    pass
