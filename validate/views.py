from django.shortcuts import render,redirect,HttpResponse
from .forms import RegisterForm

# Create your views here.

def register(request):

    return render(request,'Regi/index.html')

def acc_register(request):
    email = request.POST['email']
    password = request.POST['password']

    return HttpResponse(email+'\n'+password)

