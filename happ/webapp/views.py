from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect,HttpResponse
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Shop, Profile, Order, Item
# Create your views here.

def index(request):
	def index(request):
	if request.method == 'POST':
		user = request.POST.get('userName')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		product = ['Chocolates','Biscuits','Atta','Grains','Natural Oils','Toileteries','Fruits','Dry Fruits']
		pro = []
		a = ''

		for i in range(1,9):
			b = 'quant'+'['+str(i)+']'
			quant = request.POST.get(b)
			print(quant)
			if(int(quant) > 0):
				pro.append(product[i-1])

		print(user)
		print(email)
		print(mobile)
		print(quant)
		print(pro)
		return HttpResponse('abc')
	else:
		return render(request, 'index.html', {})
def hi(request):
    
    queryset = Shop.objects.all()
    return render(request, 'index1.html', {'queryset':queryset})

def cart(request, shopId):
    pass
