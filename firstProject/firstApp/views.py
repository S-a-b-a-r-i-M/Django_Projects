from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greet(request):
    # WRITE OUR RESPONSE IN HERE
    greet_note='<h2 style="text-align:center; color:green; margin-top:250px;"> Hi Hero...i Welcome you here </h2>'

    return HttpResponse(greet_note) # WE GIVE THE HTML VIEW AS A RESPOND