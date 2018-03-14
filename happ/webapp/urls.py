from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('hi/', views.hi, name = 'hi'),
    path('cart/<char : shopId>', views.cart, name = 'cart'),
]
