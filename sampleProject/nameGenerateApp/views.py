from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):

    time=str(datetime.date.today)

    return render(request,'start.html',{'names':'sabari'})