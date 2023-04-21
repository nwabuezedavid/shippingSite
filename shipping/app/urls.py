from django.urls import path
from . views import *

urlpatterns = [
    
    path("", home, name="home"),
    path("service/", service, name="service"),
    path("track/", track, name="tracking"),
    path("Dashboard/<pk>/", owerDashboard, name="owerDashboard"),
    path("addshopping/<pk>/", adminCreate, name="adminCreate"),
    path("blog/", blog, name="blog"),
    path("contact/", contact, name="contact"),
    path("logout/", logOutUser, name="logoutUser"),
    path("login/", LoginUser, name="LoginUser"),
    path("checkCode/<pk>/", checkCode, name="checkCode"),
    path("deleteMessage/<pk>/", deleteMessagesd, name="deleteMessagesd"),
    path("gencodcc/", gencodcc, name="gencodcc"),
    path("chattingCus/<pk>/", chattingCus, name="chattingCus"),
    path("chatting/<pk>/", chattingCusRpoom, name="chattingCusRpoom"),
    path("checkCodes/<pk>/", checkCodeADmin, name="AdmincheckCode"),
    path("edit/<pk>/", ADminEdit, name="ADminEdit"),
    path("profile/<pk>/", PROfile, name="ADminEditprofile"),
    path("update/<pk>/", asUpdate, name="asUpdate"),
    path("delete/<pk>/", delectItem, name="delectItem"),
    path("fetchat/<pk>/", fetchat, name="fetchat"),
]