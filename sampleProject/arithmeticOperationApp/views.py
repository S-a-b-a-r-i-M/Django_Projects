from django.shortcuts import render

# Create your views here.

def execute(request):
    type=request.POST['operation']
    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if type=='add':
        res = int(num1) + int(num2)
    elif type=='sub':
        res = int(num1) - int(num2)
    elif type=='mul':
        res = int(num1) * int(num2)
     
    return render(request,'operation.html',{'result':res})
