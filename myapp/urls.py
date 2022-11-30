from django.urls import path
from . import views

urlpatterns=[

    path('master/',views.masterpage,name="master"),
    path('home/',views.homepage,name="home"),
    path('register/',views.registerpage,name="register"),
    path('adminmaster/',views.admasterpage,name="adminmaster"),
    path('usermaster/',views.usermasterpage,name="usermaster"),
    path('signin/',views.signinpage,name="signin"),
    path('category/',views.catpage,name="category"),
    path('admindashboard/',views.adashpage,name="admindashboard"),
    path('shopmaster/',views.shoppage,name="shopmaster"),
    path('indoor/',views.indoorpage,name="indoor"),
    path('outdoor/',views.outdoorpage,name="outdoor"),
    path('flowering/',views.floweringpage,name="flowering"),
    path('gift/',views.giftpage,name="gift"),
    path('bonsai/',views.bonsaipage,name="bonsai"),
    path('cart/',views.cartpage,name="cart"),
    path('profile/',views.profilepage,name="profile"),


]