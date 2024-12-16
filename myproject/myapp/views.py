from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')


def hotel():
    return render("hotel.html")


def sign_in():
    return render("sign-in.html")


def help_centre():
    return render("help-centre.html")




