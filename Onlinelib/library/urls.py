from django.contrib import admin
from django.urls import path,include
from library import views

urlpatterns = [
    path('',views.index,name="index page"),
    path('index',views.index,name="index page"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('main',views.main,name="main"),
    path('contactus',views.contactus,name="contactus"),
    path('about',views.aboutus,name="aboutus"),
    path('logout',views.logout,name="logout")
]