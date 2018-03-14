from django.shortcuts import render
from . import gcm
# Create your views here.

def push(request):
    gcm.PushNotification()