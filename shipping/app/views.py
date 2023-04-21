from pickle import NONE
from queue import Empty
from wsgiref.util import request_uri

from django.contrib.messages.api import error
from django.forms.widgets import PasswordInput
from django.shortcuts import render,redirect
from . models import  detailToship,GoodsShipp,messagechat,   GenerateId,decor,chattingcustmer
# Create your views here.
import barcode
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from barcode import get_barcode_class
sitedetail  = decor.objects.first()

from django.contrib.auth.models import User
from . formupdate import *
from django.contrib.auth import authenticate, login, logout
def home(request):
    if  request.user.is_authenticated:
        return redirect('owerDashboard' , pk=request.user.id)
    activBtn = decor.objects.all().first()
    conx ={
    'activBtn':activBtn,
    'sitedetail':sitedetail,
    }
    return render(request,'html/home.html', conx)
def service(request):
    conx ={
    'sitedetail':sitedetail,
    }

    return render(request,'html/service.html', conx)
def blog(request):
    conx ={
    'sitedetail':sitedetail,
    }
    return render(request,'html/blog.html', conx)
def contact(request):
    conx ={
    'sitedetail':sitedetail,
    }
    return render(request,'html/contact.html', conx)
def track(request):
    try:
        if request.method == 'POST':
            trackerCode = request.POST['trackerCode']
            tackcomfirm = GoodsShipp.objects.get(serialNumber=trackerCode)
            return redirect('AdmincheckCode',  pk = tackcomfirm.id )
        conx ={
            'sitedetail':sitedetail,
        }
        return render(request,'html/Tracking.html', conx)
    except :
        print('sd' )
    conx ={
        'sitedetail':sitedetail,
    }
    return render(request,'html/Tracking.html', conx)


def owerDashboard(request,pk):  
    if not  request.user.is_authenticated:
         
        return redirect('LoginUser')
    user = User.objects.get(id=pk)
    
    goodsToship = GoodsShipp.objects.all()
   
    conx = {
        'items':goodsToship,
        'sitedetail':sitedetail,
    }
    
  
    return render(request,'html/map.html', conx)
def PROfile(request, pk):
    user = User.objects.get(id=pk)
   
    
    if request.method =="POST": 
        firstname = request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        lastname = request.POST['lastname']
        
        if int(sitedetail.pin) == int(password):

            user.username = username
            user.email = email
            user.first_name = firstname
            user.last_name = lastname
            
            user.save()
            messages.error(request, "updated Sucessfully ")
        else:
            messages.error(request, "Enter Your vaild Password To update")
    conx={
        'sitedetail':sitedetail,
    }
    return render(request,'adminDa/profile.html',conx )
from django.contrib.auth.hashers import make_password 
  
def ADminEdit(request, pk):
    user = User.objects.get(id=pk)
    sitedetail  = decor.objects.first()
    
    try:
        if request.method =="POST": 
            Website = request.POST['Website']
            address = request.POST['address']
            cphonenum = request.POST['cphonenum']
            cpdiscri = request.POST['cpdiscri']
            cpkw = request.POST['cpkw']
            cpurl = request.POST['cpurl']
            cpEmail = request.POST['cpEmail']
            passwordb = request.POST['pass']

            if int(sitedetail.pin) == int(passwordb):
                forms = webFormsite(request.POST,request.FILES, instance = sitedetail)
                if forms.is_valid():
                    forms.save()
                sitedetail.Website = Website
                sitedetail.address = address
                sitedetail.cphonenum = cphonenum
                sitedetail.cpdiscri = cpdiscri    
                sitedetail.cpkw = cpkw    
                sitedetail.cpurl = cpurl    
                sitedetail.cpEmail = cpEmail 
                sitedetail.save()  
                messages.error(request, "Sucessfully  updated")
            else:
                messages.error(request, "Enter Your vaild Password To update")
    except:
            messages.error(request, "Sorry something went wrong our Team are working on it")
            print('heke')
    cin = {
            'sitedetail' :sitedetail
        }    
    return render(request,'adminDa/profilemain.html' ,cin)
   
def delectItem (request, pk):
    if request.user.is_authenticated:
        user = GoodsShipp.objects.get(id=pk)
        user.delete()
        return redirect('owerDashboard', pk = request.user.id)
def LoginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            if User.objects.get(username = username, email= email):
                userAdmin= User.objects.get(username = username)
                user = authenticate(request, username=username, email=email, password=password )
                login(request,user)
                return redirect('owerDashboard' ,userAdmin.id)
            else:
                return redirect('LoginUser' )
        except: 
            
            return redirect('LoginUser' )
    no ={
        'sitedetail':sitedetail,
    }        
    return render(request,'html/login.html', no)


def adminCreate(request,pk):
    user = User.objects.get(id=pk)
    
    if request.method == "POST":
        ShipperName = request.POST['ShipperName']
        PhoneName = request.POST['PhoneName']
        email = request.POST['email']
        reciShipperName = request.POST['reciShipperName']
        recPhoneNumber = request.POST['recPhoneNumber']
        recEmail = request.POST['recEmail']
        location = request.POST['location'] 
        status = request.POST['status']
        remark = request.POST['remark']
        typeofshipp = request.POST['typeofshipp']
        weight = request.POST['weight']
        dateTime = request.POST['dateTime']
        quatity = request.POST['quatity']
        reciaddress = request.POST['reciaddress']
        shpperAddressaddress = request.POST['shpperAddressaddress']
        dispatchlocation = request.POST['dispatchlocation']
        dispatchdate = request.POST['dispatchdate']
        EstimatedDeliveryDate = request.POST['EstimatedDeliveryDate']
        currentlocation = request.POST['currentlocation']
        if request.user.is_authenticated:
            saveDetail = detailToship.objects.create(
                ShipperName = ShipperName , 
                PhoneName = PhoneName , 
                email = email , 
                reciShipperName = reciShipperName , 
                recPhoneNumber = recPhoneNumber , 
                recEmail = recEmail , 
                location = location , 
                status = status , 
                remark = remark , 
                typeofshipp = typeofshipp , 
                weight = weight , 
                dateTime = dateTime , 
                quatity = quatity , 
                reciaddress = reciaddress , 
                shpperAddressaddress = shpperAddressaddress , 
                dispatchlocation = dispatchlocation , 
                dispatchdate = dispatchdate , 
                EstimatedDeliveryDate = EstimatedDeliveryDate , 
                currentlocation = currentlocation , 
                    )
            saveDetail.save()
            codes = GoodsShipp.objects.create(product=saveDetail )
            codes.save()
            return redirect ('owerDashboard' , pk = user.id)


    conx={
        'sitedetail':sitedetail,
    }
    return render(request,'adminDa/createShipping.html', conx) 


def asUpdate(request, pk):
        
    saveDetail = detailToship.objects.get(id=pk)
    form = shippingForm(instance= saveDetail)
    
    if request.method == "POST":
        form = shippingForm(request.POST, instance= saveDetail)
        if form.is_valid(): 
            form.save()
       
        
   

            
    co = {
    'sitedetail':sitedetail,
        'form':form
    }      
    return render(request,'adminDa/updateAdmin.html',co) 



def checkCodeADmin(request,pk):
    try:
        saveDetail = GoodsShipp.objects.get(serialNumber=pk)
    except:
        JsonResponse('Error')    
    conx = {
         'saveDetail' : saveDetail,
          'sitedetail':sitedetail,
    }
    return render(request,'adminDa/CHECKTRACK.html', conx)
def checkCode(request,pk):
    saveDetail = detailToship.objects.get(id=pk)
    conx = {
        'sitedetail':sitedetail,
    }
    return render(request,'html/CHECKTRACK.html')
def logOutUser(request):
    logout(request)
    return redirect('home')


def deleteMessagesd(request, pk):
    delemessage = chattingcustmer.objects.filter(roommessagestext__roomid = pk)
    delemessage.delete()
    return redirect ('chattingCus' , pk = request.user.id)



def chattingCus(request, pk):
    
    code__roomRed = User.objects.get(id = pk)
    code__roomDetail = GenerateId.objects.all()
    code__roomDetailDw = chattingcustmer.objects.all()
    
    code__roomDetailD = chattingcustmer.objects.all()

    
    conx = {
      'code__roomRed': code__roomRed,
      'as': code__roomDetailDw,
      'mainmeeage': code__roomDetailD,
      'sitedetail':sitedetail,
      
    }
    return render(request, 'adminDa/chattPerson.html',conx)   


from .codeGen import roomcode


def gencodcc (request):
    codeRoomsd = roomcode()
    return redirect('chattingCusRpoom' , pk = codeRoomsd)

def chattingCusRpoom(request, pk):
    USuer = request.user
    code__room,d = GenerateId.objects.get_or_create(roomid = pk)
    
    
    sd = chattingcustmer.objects.get_or_create(roommessagestext = code__room )
    # print(sd.roommessagestext)
    
    conx = {
        'USuer':USuer,
        'sitedetail':sitedetail,
        'code__room':code__room,
        'idroom':code__room,
    }
    return render(request, 'adminDa/chattingRoom.html',conx)  
    
from .serili import *
from rest_framework .views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
# AJAX

@api_view(['GET', 'POST'])
def fetchat(request,pk):
    code__room,d = GenerateId.objects.get_or_create(roomid = pk)
    if request.method  == "POST":
        mams = request.data['messaga'] 
        sender = request.data['sender'] 
        maindd = chattingcustmer.objects.get(roommessagestext = code__room )
        
        maismsm = messagechat.objects.create(messaga=mams,    sender= request.user.username or None  )
        
        names = maindd.Main_messages.add(maismsm )
        serlierss = CustomerchattingApi(data = maindd)
   
        mainds  = maindd.Main_messages.last()
        serlierass = CustomerchattingApimessagechat(mainds )
        if  serlierss.is_valid() :
            serlierss.save()
            # serliers.save()
            return Response({'datamessage':serlierass.data})
        return Response({'datamessage':serlierass.data})
    if request.method =="GET":
        

        maindd = chattingcustmer.objects.get(roommessagestext = code__room )
        mainds  = maindd.Main_messages.all()
        # serlieras = CustomerchattingApi(pk)
        serlierass = CustomerchattingApimessagechat(mainds, many=True)
        serliers = CustomerchattingApi(maindd)
        return Response({'datamessage':serlierass.data,'mainc':serliers.data })
