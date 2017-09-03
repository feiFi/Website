from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .models import User
from django.contrib.auth import authenticate, login
import re

def register(request):

    return render(request,'Regi/index.html')

def acc_register(request):
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']


    if re.match("[a-zA-Z0-9]+\@+[a-zA-Z0-9]+\.+[a-zA-Z]",email) !=None and len(email)>=7:
        print(email)
    else:
            return HttpResponse('邮箱格式有误')
    if re.match("[a-zA-Z]",password) !=None or re.match("[a-z0-9]",password) !=None or re.match("[0-9A-Z]",password) !=None and len(password)>=8 and len(password)<=14:
        print(password)
    else:
        return HttpResponse('密码必须是8到14位由大小写字母和数字组成')
    if User.objects.filter(email=email):
        return HttpResponse('已注册')
    else:
        if password==repassword:
            User.objects.create_user(email, email, password)
        else:
            return HttpResponse('两次密码不一致')
    return HttpResponseRedirect('/validate/login/')
    # return HttpResponse('注册成功！')


def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'registration/login.html')

def acc_login(request):
    username = request.POST['email']
    password = request.POST['password']

    user= authenticate(username=username, password=password)
    if not user:
        user2 = User.objects.filter(email=username)
        print (user2)
        if user2:
            username2 = user2[0].username
            user = authenticate(username=username2, password=password)



        print (user)
    if user:
        return HttpResponse('登陆成功')

    else:
        return HttpResponse('请输入正确的用户名及密码')








