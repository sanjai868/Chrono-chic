from django.db import models

# Create your models here.
class Regform(models.Model):
    name = models.CharField(max_length=255)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    phone=models.BigIntegerField()
    address=models.TextField()
    

class Login(models.Model):
    uname=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    utype=models.CharField(max_length=10)
    uid=models.ForeignKey(Regform,on_delete=models.CASCADE)

class Product(models.Model):
    pname=models.CharField(max_length=200)
    price=models.IntegerField()
    pimage=models.ImageField(upload_to='file')
    description=models.CharField(max_length=200)

class cart(models.Model):
    date=models.DateField()
    uid=models.ForeignKey(Regform,models.CASCADE)
    pid=models.ForeignKey(Product,models.CASCADE)
    qty=models.IntegerField()
    total=models.IntegerField()

class ordermaster(models.Model):
    uid=models.ForeignKey(Regform,models.CASCADE)
    date=models.DateField()
    gtotal=models.IntegerField()

class orderchild(models.Model):
    oid=models.ForeignKey(ordermaster,models.CASCADE)
    pid=models.ForeignKey(Product,models.CASCADE)
    qty=models.IntegerField(default=0)
    total=models.IntegerField()
    status=models.CharField(max_length=20)
