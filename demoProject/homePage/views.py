from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    msg='<h1 style="text-align:center; margin:350px auto 0px; color:orange" >Welcome to my demo project....<br><br> <h2 style="border:2px solid green; color:orange; text-align:center;">HomePage</h2></h1>  '
    return HttpResponse(msg)


