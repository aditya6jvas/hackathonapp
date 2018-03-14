from django.urls import path, include
from . import views

urlpatterns = [
    path('addShop/', views.addShop, name ='addShop'),
    path('addItem/', views.addItem, name = 'addItem'),
    path('viewItems', views.viewItems, name = 'viewItems'),
    path('viewOrders/', views.viewOrder, name = 'viewOrder'),
]
