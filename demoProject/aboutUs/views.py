from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def about(request):
    msg = '<h1 style="text-align:center; margin:350px auto 0px; color:red" >Welcome to my demo project....<br><br> <h2 style="border:2px solid blue; color:red; text-align:center;">Aboutus</h2></h1>'
    return HttpResponse(msg)


def contact(request):
    msg = "<h2>Address<h2>"
    return HttpResponse(msg)
