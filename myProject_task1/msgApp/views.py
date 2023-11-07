from django.shortcuts import render
from myProject_task1.celery import send_message
from django.http import HttpResponse

# Create your views here.

def push_message_to_celery(request):
    messages = ['im using celery','celery using redis','im printing the message']
    for msg in messages:
        send_message.delay(msg)

    return HttpResponse("Messages are pushed to Celery")
