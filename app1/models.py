from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class register(models.Model):
    name = models.CharField(max_length=100)
    email =models.EmailField()
    Mobilenumber = models.CharField(max_length =10)
    password = models.CharField(max_length=50)
    Address = models.TextField()
    
    def __str__(self):
        return self.name
    
class catgo(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.name

class feedb(models.Model):
    name = models.TextField()
    email = models.EmailField()
    feedback = models.TextField()
    
    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='proimg')
    qty = models.IntegerField()
    discription = models.TextField()
    price = models.CharField(max_length = 5)
    category = models.ForeignKey(catgo,on_delete = models.CASCADE)
    vendorid = models.CharField(max_length=20,default= ' ')
    
    def __str__(self):
        return self.name
    
class cart(models.Model):
    userid = models.CharField(max_length = 5)
    productid =models.CharField(max_length = 5)
    quantity = models.IntegerField()
    orderid = models.CharField(max_length =  5)
    totalprice = models.CharField(max_length = 5,default = ' ')
    
    def __str__(self):
        return self.userid
    
class vendor(models.Model):
    name = models.CharField(max_length=100)
    email =models.EmailField()
    Mobilenumber = models.CharField(max_length =10)
    password = models.CharField(max_length=50)
    Address = models.TextField()
    tob = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    
class order(models.Model):
    userid = models.CharField(max_length = 10)
    productid = models.CharField(max_length = 10)
    address = models.TextField()
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 30)
    pincode = models.CharField(max_length = 6)
    paymenttype = models.CharField(max_length = 20)
    transactionid = models.CharField(max_length = 50)
    datetime = models.DateTimeField(auto_now =  True)
    
    def __str__(self):
        return self.userid