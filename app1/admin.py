from django.contrib import admin
from .models import *
# Register your models here.
class blog_(admin.ModelAdmin):
    list_display = ['id','name', 'tagline']
    list_filter = ['name', 'tagline']
    search_fields = ['name', 'tagline']
    
class author_(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email'] 
    
class register_(admin.ModelAdmin):
    list_display = ['id','name', 'email','Mobilenumber','password','Address']
    list_filter = ['name', 'email','Mobilenumber','password','Address']
    search_fields = ['name', 'email','Mobilenumber','password','Address'] 
    
class catgo_(admin.ModelAdmin):
    list_display = ['id','name', 'image']
    
class feedb_(admin.ModelAdmin):
    list_display = ['id','name', 'email','feedback']


class pro_(admin.ModelAdmin):
    list_display = ['id','name', 'qty','price','discription','category','vendorid']

class cart_(admin.ModelAdmin):
    list_display = ['id','userid','productid','quantity','orderid','totalprice']

class vendors_(admin.ModelAdmin):
    list_display = ['id','name', 'email','Mobilenumber','password','Address','tob']
    
class order_(admin.ModelAdmin):
    list_display = ['id','userid','productid', 'address','city','state','pincode','paymenttype','transactionid','datetime']

admin.site.register(Blog,blog_)
admin.site.register(Author,author_)
admin.site.register(register,register_)
admin.site.register(vendor,vendors_)
admin.site.register(catgo,catgo_)
admin.site.register(feedb,feedb_)
admin.site.register(product,pro_)
admin.site.register(cart,cart_)
admin.site.register(order,order_)
#category table 2 columns name image type of image find