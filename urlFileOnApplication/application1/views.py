from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def start(request):
    msg="<h2>started my application1 on urlFileOnApplication</h2>"
    return HttpResponse(msg)