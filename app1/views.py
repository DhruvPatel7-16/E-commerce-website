from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.

def first(request):
    return HttpResponse("This is my first function inside django showing message")

def second(request):
    return render(request, 'demo.html')

def table(request):
    # always right logic in this file.
    a = register.objects.get(name = 's')
    # for i in a:
    #     print(i.Mobilenumber)
    return render(request, 'table.html',{'data': a})

def index(request):
    if 'email' in request.session:
        b = register.objects.get(email =request.session['email'])
        a= catgo.objects.all()
        return render(request,'index.html',{'cat':a,'session': b})
    elif 'venemail' in request.session:
        b = vendor.objects.get(email =request.session['venemail'])
        a= catgo.objects.all()
        return render(request,'index.html',{'cat': a,'vensession': b})
    else:
        a= catgo.objects.all()
        return render(request,'index.html',{'cat': a})
      

def cat(request):
    if 'email' in request.session:
        b = register.objects.get(email = request.session['email'])
        a = catgo.objects.all()
        return render(request, 'cat.html',{'cat' : a,'session' : b})
    else:
         a = catgo.objects.all()
         return render(request, 'cat.html',{'cat' : a})
        
        
    
def reg(request):
    if request.method == 'POST':
        a = register()
        a.name = request.POST['uname']
        a.email = request.POST['email']
        a.mob = request.POST['mob']
        a.add = request.POST['add']
        a.password = request.POST['password']
        a.cp= request.POST['cp']
        b = register.objects.filter(email = request.POST['email'] )
        error_msg = None
        if a.email:
            if b:
                return render(request, 'register.html', {'email': 'this email is already registered'})
            else:    
                if len(a.mob) == 10:
                    if request.POST['password'] == request.POST['cp']:
                        a.save()
                        return render(request, 'register.html', {'save': 'Data stored succesfully'})
                    else:
                        return render(request, 'register.html', {'pass': 'passwords did not match'})
                else:
                    error_msg = "Mobile number must be 10 digits."
                    return render(request, 'register.html', {'error': error_msg})
        else:
             error_msg = "Email field is mandatory!!"       
             return render(request,'register.html', {'error': error_msg })  
    else:
         return render(request, 'register.html', {'save': 'Data stored succesfully'})
def nav(request):
    return render(request, 'nav.html')



def data(request):
    if request.method == 'POST':
        a = Blog()
        a.name = request.POST['uname']
        a.tagline = request.POST['data']
        a.save()
        print("data stored successfully...")
        return render(request,'store.html')

    else:
        print("failed to store data... ")
        return render(request,'store.html')
    
def img(request):
    if request.method == 'POST':
        a = catgo()
        a.name = request.POST['uname']
        a.image = request.FILES['img']
        a.save()
        print("image uploaded successfully...")
        return render(request,'img.html')
    else:
        print("failed to upload image...") 
        return render (request,'img.html')
    
    
from django.core.mail import send_mail
from django.conf import settings

def feed(request):
    if request.method == 'POST':
            a = feedb()
            a.name = request.POST['uname']
            a.email = request.POST['email']
            a.feedback=request.POST['feed']
                
            send_mail('authentication email for',
            'This is a mail to check if you recieved an email or not',
            'dhruv6615patel@gmail.com',
            [a.email],
            fail_silently= False
            )
            a.save()
            return render(request, 'feed.html')
    else:
        return render(request, 'feed.html')
    
def login(request):
    if request.method == 'POST':
        try:
            a = register.objects.get(email = request.POST['email'])
            if a.password == request.POST['password']:
                request.session['email']= a.email
                request.session['userid']= a.pk
                print(request.session['email'],"2212121222212")
                return redirect('index')
            else:
                return render(request,'login.html',{'login':'Invalid credentials!!!'})
    
        except:
                 return render(request,'login.html',{'reg':'Registration is required'})
    else:
        return render(request,'login.html')        
            
def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect('cat')
    elif 'venemail' in request.session:
        del request.session['venemail']
        return redirect('index')
    else:
        return redirect('index')

def profile(request):
    if 'email' in request.session:
        a = register.objects.get(email = request.session['email'])
        if request.method == 'POST':
            a.name = request.POST['uname']
            a.mob = request.POST['mob']
            a.add = request.POST['add']
            a.save()
            return render(request,'profile.html',{'prof': a,'update': "data updated successfully", 'session': a})
        else:
            return render(request,'profile.html',{'prof': a,'session': a})
        
    else:
        return redirect('login')
    
def changepass(request):
    if 'email' in request.session:
        a = register.objects.get(email = request.session['email'])
        if request.method == 'POST':
            print(1111111)
            if a.password == request.POST['op']:
                    print(2222222)
                    if request.POST['np'] == request.POST['cp']:
                        print(333333)
                        a.password = request.POST['np']
                        a.save()
                        return render(request,'pass.html')
                    else:
                        return render(request,'pass.html',{'confirm': "new password did not matched!"})
            else:
                return render(request,'pass.html',{'wrongp': "Old password is wrong!!"})
        else:
                return render(request,'pass.html')
    else:
        return redirect('login')
def card(request,id):
    if 'email' in request.session:
        a=catgo.objects.get(id = id)
        return render(request,'card.html',{'a': a})
    else:
        return redirect('login')
    
    
def pro(request,id):
     if 'email' in request.session:
        b = register.objects.get(email =request.session['email'])
        a = product.objects.filter(category = id)
        return render(request,'pro.html',{'pro': a,'session': b})
     else:
        return redirect('login')
    
def prodetails(request,id):
    if 'email' in request.session:
        a = register.objects.get(email =request.session['email'])
        b = product.objects.get(id = id)
        if request.method == 'POST':
            c = cart()
            c.productid = id
            c.userid = request.session['userid']
            c.quantity = request.POST['qty']
            c.totalprice = int(request.POST['qty']) * int(b.price)
            c.orderid = "0"
            d = cart.objects.filter(productid = id,userid = request.session['userid'],orderid = "0")
            if d:
                print("allready in cart")
                return render(request,'product.html',{'session': a,'prod': b,'chhej':'chhejjjj!!!' })
            else:
                 print("nathi")
                 if b.qty <= 0:
                    print("pati gyu")
                    return render(request,'product.html',{'session': a,'prod': b,'stock':'Out of stock' })
                 else:
                    print("stock ma chhe")
                    if int(request.POST['qty']) > b.qty:
                        print("bau vadhare thai gyu")
                        return render(request,'product.html',{'session': a,'prod': b,'max':'ochhi kar' })
                    else:
                        print("save done")
                        c.save()
                        b.qty = b.qty - int(request.POST['qty'])
                        b.save()
                        return render(request,'product.html',{'session': a,'prod': b})
        else:
            return render(request,'product.html',{'session': a,'prod': b})
    else:
        return redirect('login')
    
def cartdata(request):
    if 'email' in request.session:
        a = register.objects.get(email =request.session['email'])
        b = cart.objects.filter(userid = request.session['userid'], orderid = "0" )
        prolist = []
        total = 0
        if b:
            request.session['cartdata'] = True 
            for i in b:
                total += int(i.totalprice)
                pro = product.objects.get(id = i.productid )
                prodict = {'id': i.productid, 'proimage': pro.image,'proprice': pro.price,'prodis': pro.discription,'qty':i.quantity,'total': i.totalprice}
                prolist.append(prodict)
            
                if 'stock' in request.session: 
                    del request.session['stock']
                    return render(request,'cart.html',{'session' : a,'prolist': prolist,'grandtotal': total,
                    'stock':"khatam tata bye bye" })
                else:
                    return render(request,'cart.html',{'session' : a,'prolist': prolist,'grandtotal': total,'cartdata': request.session['cartdata']})
        else:
            return render(request,'cart.html',{'session' : a,'prolist': prolist,'grandtotal': total})

    else:
        return redirect('login')
    
def additem(request,id):
    a = cart.objects.get(productid = id , userid = request.session['userid'])
    b = product.objects.get(id = a.productid)
    if b.qty <= 0:
        request.session['stock'] = 0
        return redirect('cart')
    else:
        a.quantity = int(a.quantity) + 1
        a.totalprice = int(a.totalprice) + int(b.price)
        a.save()
        b.qty = int(b.qty) - 1
        b.save()
        return redirect('cart')
        
    
def minus(request,id):
    if 'email' in request.session:
        a = cart.objects.get(productid = id , userid = request.session['userid'])
        b = product.objects.get(id = a.productid)
        if a.quantity <= 1:
            a.delete()
            return redirect('cart')
        else:
            a.quantity = int(a.quantity) - 1
            a.totalprice = int(a.totalprice) - int(b.price)
            a.save()
            b.qty = int(b.qty) + 1
            b.save()
            return redirect('cart')
    else:
        return render('login')
    
    
def removeall(request):
    if 'email' in request.session:
        c = cart.objects.filter(userid=request.session['userid'])
        for i in c:
            a = product.objects.get(id = i.productid )
            a.qty = int(a.qty )+ int(i.quantity)
            a.save()
            c.delete()
            return redirect('cart')
    else:
        return render('login')
    
def remove(request,id):
    if 'email' in request.session:
        c = cart.objects.get(userid = request.session['userid'],productid = id)
        a = product.objects.get(id=c.productid)
        a.qty = int(a.qty )+ int(c.quantity)        
        a.save()
        c.delete()
        return redirect('cart')
    else:
        return render('login')
    
    
def checkout(request):
    if 'email' in request.session:
        a = register.objects.get(email=request.session['email'])
        cartdata = cart.objects.filter(userid=request.session['userid'], orderid = "0")
        prolist = []
        proidlist = []
        amount = 0
        for i in cartdata:
            amount = amount + int(i.totalprice)
            pro = product.objects.get(id=i.productid)
            prodict = {'proimg': pro.image,'proname':pro.name,'prodis': pro.discription,'proprice':pro.price,'cartqty': i.quantity,'carttprice': i.totalprice}
            prolist.append(prodict)
            proidlist.append(pro.pk)  
            
        if request.method == 'POST':
            orderdata = order()
            orderdata.userid = request.session['userid']  
            orderdata.productid = proidlist
            orderdata.address = request.POST['add']  
            orderdata.city = request.POST['city']  
            orderdata.state = request.POST['state']  
            orderdata.pincode = request.POST['pincode']  
            orderdata.paymenttype = request.POST['paymentvia'] 
            
            if orderdata.paymenttype == "cod":
                orderdata.transactionid = '12345'
                orderdata.save()
                latestorderid = order.objects.latest('id')
                for i in cartdata:
                    i.orderid = latestorderid.pk
                    i.save()
                return render(request,'index.html',{'prolist': prolist,'amount': amount,'session': a})   
            else:
                request.session['finalamount'] = amount
                request.session['productid'] = proidlist
                request.session['add']  = request.POST['add']  
                request.session['city']  = request.POST['city']
                request.session['state']  = request.POST['state']
                request.session['country']  = request.POST['country']
                request.session['pincode']  = request.POST['pincode']
                request.session['payment']  = request.POST['paymentvia']
                return redirect('razorpay')
        else:
            return render(request,'checkout.html',{'prolist': prolist,'amount': amount,'session': a}) 
    else:
        return redirect('login')
    
    
RAZOR_KEY_ID = 'rzp_test_LKEffZFPhUKToo'
RAZOR_KEY_SECRET = 'P5THlIMOpyODuy4i8BkZMCiw'    

import razorpay
razorpay_client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

def razorpayview(request):
    currency = 'INR'
    amount = int(request.session['finalamount']) * 100
    
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0')) 
    razorpay_order_id = razorpay_order['id'] 
    callback_url = 'http://127.0.0.1:8000/paymenthandler/'
    
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    
    return render (request, 'razorpay.html', context= context)



from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

@csrf_exempt
def paymenthandler(request):
    if request.method == 'POST':
        try:
            payment_id = request.POST.get('razorpay_payment_id','')
            razorpay_order_id = request.POST.get('razorpay_order_id','')
            signature = request.POST.get('razorpay_signature','')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            amount = int(request.session['finalamount']) * 100
            razorpay_client.payment.capture(payment_id, amount)
            orderdata = order()
            orderdata.userid = request.session['userid']  
            orderdata.productid = request.session['productid']  
            orderdata.address = request.session['add']  
            orderdata.city = request.session['city']  
            orderdata.state = request.session['state']  
            orderdata.pincode = request.session['pincode']  
            orderdata.paymenttype = request.session['payment'] 
            orderdata.trasactionid = payment_id
            orderdata.save()
            cartdata = cart.objects.filter(userid=request.session['userid'], orderid = "0")
            latestorderid = order.objects.latest('id')
            for i in cartdata:
                i.orderid = latestorderid.pk
                i.save()
            return render(request, 'success.html')
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()
    
    
def orderhistory(request):
    if 'email' in request.session:
        a = cart.objects.filter(userid = request.session['userid'])
        prolist = []
        for i in a:
            if i.orderid != "0":
                prodetails = product.objects.get(id = i.productid)
                orderdt = order.objects.get(id = i.orderid)
                prodict = {'orderid': i.orderid,'qty' : i.quantity,'totalprice': i.totalprice,'proname' : prodetails.name, 'proimg': prodetails.image,'prodis': prodetails.discription,'proprice': prodetails.price,'datetime' : orderdt.datetime}
                prolist.append(prodict)
        return render(request,'orderhistory.html',{'session': True})
    else:
        return redirect('login')
    
# vendorside

def vendorreg(request):
    if request.method == 'POST':
        a = vendor()
        a.name = request.POST['uname']
        a.email = request.POST['email']
        a.mob = request.POST['mob']
        a.add = request.POST['add']
        a.password = request.POST['password']
        a.cp= request.POST['cp']
        a.tob = request.POST['tob']
        a.save()
        b = catgo.objects.filter(name = a.tob)
        if b:
            b.save()
            return render(request,'register.html',{'forvendor':'venreg'})
        else:    
            return redirect('img')
    else:    
        return render(request,'register.html',{'forvendor':'venreg'})
    
    
def vendlogin(request):
    if request.method == 'POST':
        try:
            a = vendor.objects.get(email = request.POST['email'])
            if a.password == request.POST['password']:
                request.session['venemail']= a.email
                request.session['venid']= a.pk
                print(request.session['venemail'],"2212121222212")
                return redirect('index')
            else:
                return render(request,'login.html',{'login':'Invalid credentials!!!'})
    
        except:
                 return render(request,'login.html',{'reg':'Registration is required'})
    else:
        return render(request,'login.html')
    
def addpro(request):
    if 'venemail' in request.session:
        a = catgo.objects.all()
        if request.method == 'POST': 
            b = product()
            b.name = request.POST['cname']
            b.qty = request.POST['stock']
            b.price = request.POST['price']
            d = request.POST['cat']
            c = catgo.objects.get(pk = d)
            b.category = c
            print(d,"1111111")
            b.discription = request.POST['des']
            b.image = request.FILES['image']
            b.vendorid = request.session['venid']
            b.save()
            return render(request,'addpro.html',{'cat': a})
        else:        
            return render(request,'addpro.html',{'cat': a})
 
    else:
        return redirect('venlogin')
    
def addcat(request):
    if request.method == 'POST':
        a = catgo()
        a.name = request.POST['uname']
        a.image = request.FILES['img']
        a.save()
        print("image uploaded successfully...")
        return render(request,'addcat.html')
    else:
        print("failed to upload image...") 
        return render(request,'addcat.html')
    
def venpro(request):
    if 'venemail' in request.session:
        a = product.objects.filter(vendorid = request.session['venid'])
        return render(request,'venpro.html',{'vensession':'venreg','prod' : a})
    else:
        return redirect('venlogin')

def updatepro(request,id):
    if 'venemail' in request.session:
        a = product.objects.get(id = id)
        if request.method == 'POST':
            a.name = request.POST['pname']
            a.price = request.POST['price']
            a.qty = request.POST['qty']
            a.discription = request.POST['dis']
            a.image = request.FILES['img']
            a.save()
            return render(request,'updatepro.html',{'a': a})
        else:
            return render(request,'updatepro.html',{'a': a})            
    else:
        return redirect('venlogin')

def deletepro(request,id):
    if 'venemail' in request.session:
        a = product.objects.get(id = id)
        a.delete()
        return redirect('venpro')            
    else:
        return redirect('venlogin')
    
def soldpro(request):
    if 'venemail' in request.session:
        a = cart.objects.all()
        prolist = []
        for i in a:
            if i.orderid != "0":
                b = product.objects.get(id = i.productid)
                if int(b.vendorid) == int(request.session['venid']):
                    dt = order.objects.get(id = i.orderid)
                    prodict = {'proimg' : b.image,'proname' : b.name,'proprice' : b.price,'prodis': b.discription,'orderid': i.orderid,'datetime': dt.datetime,'qty': i.quantity,'total': i.totalprice}
                    prolist.append(prodict)
        return render(request,'soldpro.html',{'prolist':prolist,'vensession' : True})
    else:
        return redirect('venlogin')