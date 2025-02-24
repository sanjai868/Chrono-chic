from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from myapp.models import Regform,Login,Product,cart,ordermaster,orderchild
import datetime

# Create your views here.
def home(request):
    template=loader.get_template("home.html")
    context={}
    return HttpResponse(template.render(context,request))

def login(request):
    if request.method == 'POST':
        uname=request.POST.get('uname')
        upass=request.POST.get('password')
        if Login.objects.filter(uname=uname,password=upass):
            l=Login.objects.get(uname=uname,password=upass)
            request.session["uid"]=l.uid_id
            if l.utype=='user': 
                return HttpResponse("<script>alert('Welcome User');window.location='/products';</script>")
            elif l.utype=='admin':
                return HttpResponse("<script>alert('Welcome Admin');window.location='/adminhm';</script>")
            else:
                return HttpResponse("<script>alert('Invalid User');window.location='/login';</script>")
        else:
            return HttpResponse("<script>alert('Invalid User Type');window.location='/login';</script>")
    else:
        template=loader.get_template("login.html")
        context={}
        return HttpResponse(template.render(context,request))

def regform(request):
    if request.method=="POST":
        r=Regform()
        r.name=request.POST.get('name')
        r.age=request.POST.get('age')
        r.gender=request.POST.get('gender')
        r.email=request.POST.get('email')
        r.phone=request.POST.get('phone')
        r.address=request.POST.get('address')
        r.save()
        id=Regform.objects.latest("id").id
        l=Login()
        l.uname=request.POST.get('username')
        l.password=request.POST.get('password')
        l.utype='user'
        l.uid_id=id
        l.save()
        return HttpResponse("<script>alert('Registration Successsfull');window.location='/logincd';</script>")
    else:
        template=loader.get_template("regform.html")
        context={}
        return HttpResponse(template.render(context,request))

def products(request):
    template=loader.get_template("products.html")
    context={}
    return HttpResponse(template.render(context,request))

def adminhm(request):
    template=loader.get_template("adminhm.html")
    context={}
    return HttpResponse(template.render(context,request))

def addprdct(request):
    if request.method=="POST":
        p=Product()
        p.pname=request.POST.get('name')
        p.price=request.POST.get('price')
        p.pimage=request.FILES['image']
        p.description=request.POST.get('description')
        p.save()
        return HttpResponse("<script>alert('Product Added Successfully');window.location='/addprdct';</script>")
    else:
        template=loader.get_template("addprdct.html")
        context={}
        return HttpResponse(template.render(context,request))

def products(request):
        v=Product.objects.all()
        template=loader.get_template("products.html")
        context={'data':v}
        return HttpResponse(template.render(context,request))

def proview(request,id):
    v=Product.objects.get(id=id)
    request.session["pid"]=id
    template=loader.get_template("proview.html")
    context={'data':v}
    return HttpResponse(template.render(context,request))

def Cart(request):
    if request.method == "POST":
        c = cart()
        data = Product.objects.get(id=request.session["pid"])
        c.date = datetime.datetime.today()
        c.qty = int(request.POST.get('qty'))
        c.total = c.qty * data.price
        c.pid_id = data.id
        c.uid_id = request.session['uid']
        c.save()
        return HttpResponse("<script>alert('Item added to cart');window.location='/viewcart';</script>")

def viewcart(request):
    if request.method == "POST":
        c=cart.objects.all()
        om=ordermaster()
        om.uid_id=request.session['uid']
        om.date=datetime.datetime.today()
        om.gtotal =1000
        om.save()
        oid=ordermaster.objects.latest('id').id
        for i in c:
            oc=orderchild()
            oc.oid_id=oid
            oc.pid_id=i.pid_id
            oc.qty=i.qty
            oc.total=i.total
            oc.status='Ordered'
            oc.save()
        c.delete()
        return HttpResponse("<script>alert('Order Placed Successfully');window.location='/vieworder';</script>")
    else:
        cart_items=cart.objects.raw("select myapp_product.pname,myapp_cart.* from myapp_product,myapp_cart where myapp_product.id=myapp_cart.pid_id")
        # cart_items = cart.objects.filter(uid_id=request.session.get('uid'))
        grand_total = sum(item.total for item in cart_items)
        template = loader.get_template('viewcart.html')
        context = {'data': cart_items, 'grand_total': grand_total}
        return HttpResponse(template.render(context, request))
    
def vieworder(request):
    d=ordermaster.objects.raw("select * from myapp_ordermaster,myapp_orderchild,myapp_product where myapp_product.id=myapp_orderchild.pid_id and myapp_orderchild.oid_id=myapp_ordermaster.id and myapp_ordermaster.uid_id=%s",[request.session["uid"]])
    template=loader.get_template("vieworder.html")
    context={'data':d}
    return HttpResponse(template.render(context,request))

def delete(request,id):
    if request.method == "POST":
        v= get_object_or_404(cart,id=id)
        v.delete()
        return HttpResponse("<script>alert('Item deleted from cart');window.location='/viewcart';</script>")
    
def cancelord(request, oid_id):
    if request.method == "POST":
        v = orderchild.objects.get(oid_id=oid_id)
        v.delete()
        return HttpResponse("<script>alert('Order cancelled');window.location='/vieworder';</script>")
    else:
        return HttpResponse("<script>alert('Invalid request');window.location='/vieworder';</script>")