from django.urls import path, include
from . import views

urlpatterns = [
    path('addShop/', views.addShop, name ='addShop'),
    path('addItem/', views.addItem, name = 'addItem'),
    path('viewItems/', views.viewItems, name = 'viewItems'),
    path('waitingOrders/', views.waitingOrder, name = 'waitingOrder'),
    path('confirmedOrders/', views.confirmedOrder, name = 'confirmedOrder'),
    path('killedOrders/', views.killedOrder, name = 'killedOrder'),
    path('singleOrder/', views.singleOrder, name = 'singleOrder'),
    path('singleItem/', views.singleItem, name = 'singleItem'),
    path('editItem/', views.editItem, name = 'editItem'),
    path('acceptOrder/', views.acceptOrder, name  = 'acceptOrder'),
    path('killOrder/', views.killOrder, name = 'killOrder'),   
]
