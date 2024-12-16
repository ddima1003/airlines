from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path("/hotel",views.hotel),
    path("/sign-in",views.sign_in),
    path("/help-centre",views.help_centre)



]