from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def getTime(request):
    time = datetime.datetime.now()
    # first datetime -> module  , second datetime -> class , now() -> method of datetime class
    msg = "The time is :" + str(time)
    msg = '<h1 style="text-align:center; margin:350px auto 0px; color:dark-blue">{}<h1>'.format(msg)
    return HttpResponse(msg)
