from signal import default_int_handler
from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
# from barcode.writer import ImageWriter
from django.core.files import File
import barcode
from random import randrange
import random
from barcode import EAN13
from barcode.writer import SVGWriter
from barcode import get_barcode_class
from io import BytesIO

from barcode import EAN13
from barcode.writer import ImageWriter

# Write to a file-like object:

# from . codeGen import serialCode 
class detailToship(models.Model):
    ShipperName = models.CharField( max_length=50 , blank=True, null=True)
    PhoneName = models.IntegerField( blank=True, null=True)
    email = models.CharField( max_length=50 , blank=True, null=True)
    reciShipperName = models.CharField( max_length=50 , blank=True, null=True)
    recPhoneNumber = models.IntegerField( blank=True, null=True)
    recEmail = models.EmailField( max_length=254 , blank=True, null=True)
    location = models.CharField( max_length=50 , blank=True, null=True)
    status = models.CharField( max_length=50 , blank=True, null=True)
    remark = models.CharField( max_length=50 , blank=True, null=True)
    typeofshipp = models.CharField( max_length=50 , blank=True, null=True)
    weight = models.CharField( max_length=900000, blank=True, null=True)
    reciaddress = models.CharField( max_length=50, blank=True, null=True)
    shpperAddressaddress = models.CharField( max_length=50, blank=True, null=True)
    dateTime = models.DateTimeField( blank=True, null=True)
    dispatchlocation = models.CharField( max_length=50, blank=True, null=True)
    dispatchdate = models.DateTimeField(  blank=True, null=True)

    EstimatedDeliveryDate = models.DateTimeField( blank=True, null=True)
    currentlocation = models.CharField( max_length=50, blank=True, null=True)
    quatity = models.CharField( max_length=50, blank=True, null=True)
    def __str__(self):
        return self.reciShipperName
class GoodsShipp(models.Model):
    product = models.ForeignKey(detailToship, on_delete=models.CASCADE , blank=True, null=True)
    serialNumber = models.CharField( max_length=50 , blank=True)
    BarIMage = models.FileField( blank=True)
    dataShipped = models.DateTimeField( auto_now=True, auto_now_add=False)
    
    def save(self, *args, **kwargs):
        if self.serialNumber == "":
            mylist = ""
            for i in range(0,13):
                x = random.randint(1,10)
                mylist += str(x)
        
            self.serialNumber = mylist
           
            EAN = barcode.get_barcode_class('ean13')
            my_ean = EAN(mylist, writer=ImageWriter())
            buffer = BytesIO()
            my_ean.write(buffer)
            self.BarIMage.save('sdsd.png',File(buffer), save=False)

            # self.BarIMage(files=ler, save=False)
        super().save(*args, **kwargs) # Call the real save() method
   
    class Meta:
        verbose_name = ("Product Own Section")
    def __str__(self):
        return f" the Reciever   {self.product.reciShipperName}"
    



class GenerateId(models.Model):
    roomid = models.CharField( max_length=330,blank=True)
    
    class Meta:
        verbose_name = ("room id custmer ")

    def __str__(self):
        return  self.roomid[:12]
class messagechat(models.Model):
    messaga = models.TextField(blank=True)
    sender = models.CharField( max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = (" Main mesaage")

    
    def __str__(self):
        return  f" the Sender is  {self.messaga[:12]}"

  







        
class chattingcustmer(models.Model):
    Main_messages = models.ManyToManyField(messagechat,blank=True)
    dated = models.DateTimeField( auto_now=True)
    roommessagestext = models.ForeignKey(GenerateId, on_delete=models.CASCADE,blank=True, null=True)
    class Meta:
        verbose_name = ("message by  custmer")
        verbose_name_plural = ("chatting custmers ")
# Create your models here.
    def __str__(self):
        return  f" the Sender is  {self.Main_messages}"

    


   

class decor(models.Model):
    Website = models.CharField( max_length=50   ,blank=True, null=True)
    address = models.CharField( max_length=50   ,blank=True, null=True)
    cphonenum = models.CharField( max_length=50   ,blank=True, null=True)
    cpdiscri = models.CharField( max_length=50   ,blank=True, null=True)
    pin = models.CharField( max_length=50   ,blank=True, null=True)
    cpkw = models.TextField( blank=True, null=True)
    cpurl = models.CharField( max_length=50   ,blank=True, null=True)
    cpEmail = models.CharField( max_length=50   ,blank=True, null=True)
    backGround = models.ImageField(upload_to='back/' ,max_length=3000000,blank=True, null=True)
    logo = models.ImageField(upload_to='logo/' ,max_length=3000000,blank=True, null=True)
    
    def __str__(self):
        return f" the name of the company{self.Website}"
        
    class Meta:
        verbose_name = ("site detail")
        verbose_name_plural = ("sites")

    

