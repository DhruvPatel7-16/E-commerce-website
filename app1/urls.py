
from django.urls import path,include
from .views import *


urlpatterns = [
    path('first/',first),
    path('table/',table,name = 'table'),
    path('cat/',cat,name = 'cat'),
    path('register/',reg,name = 'reg'),
    path('nav/',nav,name = 'nav'),
    path('data/', data,name = 'data'),
    path('image/', img,name = 'img'),
    path('feedb/',feed,name = 'feed'),
    path('login/',login,name = 'login'),
    path('logout/',logout,name= 'logout'),
    path('profile/',profile,name = 'profile'),
    path('cp/',changepass,name = 'pass'),
    path('card/<int:id>',card,name = 'card'),
    path('',index, name = 'index'),
    path('pro/<int:id>',pro, name = 'pro'),
    path('prodetails/<int:id>',prodetails, name = 'prodetails'),
    path('cart/',cartdata, name = 'cart'), 
    path('add/<int:id>',additem, name='add'),
    path('minus/<int:id>',minus, name='minus'),
    path('removeall/',removeall, name='removeall'),
    path('remove/<int:id>',remove, name='remove'),
    path('venreg/',vendorreg, name='venreg'),
    path('vendlogin/',vendlogin, name='venlogin'),
    path('addpro/',addpro, name='addpro'),
    path('addcat/',addcat, name='addcat'),
    path('venpro/',venpro, name='venpro'),
    path('updatepro/<int:id>',updatepro, name='updatepro'),
    path('deletepro/<int:id>',deletepro, name='deletepro'),
    path('checkout/',checkout, name='checkout'),
    path('soldpro/', soldpro, name= 'soldpro'),
    path('razorpayview/',razorpayview, name= 'razorpay'),
    path('paymenthandler/',paymenthandler, name= 'paymethandler'),
    path('orderhistory/',orderhistory, name= 'orderhistory')
    ]