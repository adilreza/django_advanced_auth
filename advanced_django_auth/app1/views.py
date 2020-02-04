from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import datetime


# Create your views here.



def registration(request):
    return render(request ,'registration.html')

def logout_now(request):
    html = "<h1>I am from logout request</h1>";
    logout(request)
    return  HttpResponse(html)

def permited(request):
    user = authenticate(username='Adil', password='123456')
    if user:
        print(user)
        login(request, user)

    if request.user.is_authenticated:
        print(request.user);
        return render(request, 'permited.html')
    else:
        return render(request, 'denied.html')

# def permited(request):
#     user = authenticate(username='Adil', password='1234')
#     if user is not None:
#         return render(request, 'permited.html');
#     else:
#         return render(request, 'denied.html');


def common(request):
    #user_name_c= "Adil";
    #user = User.objects.get_by_natural_key(username=user_name_c)
    #user.last_name="Reza";
    #user.save();
    return render(request, 'common.html')

def registration_post(request):
    fname = request.POST.get('fname');
    user_name = fname
    #print(fname);
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.create_user(user_name,email,password);
    user.save();
    return render(request, 'page2.html')