from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def product(request):
    msg = '<h1 style="text-align:center; margin:350px auto 0px; color:darkgreen" >Welcome to my demo project....<br><br> <h2 style="border:2px solid black; color:darkgreen; text-align:center;">Products</h2></h1>'
    return HttpResponse(msg)
