from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect,HttpResponse
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def hi(request):
    return render(request, 'index1.html', {})
