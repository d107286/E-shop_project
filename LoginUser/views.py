import hashlib
from django.shortcuts import render,HttpResponseRedirect
from LoginUser.models import *


def setPassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result

def register(request):
    error_message=''
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if email:
            user=LoginUser.objects.filter(email=email).first()
            if not user:
                new_user=LoginUser()
                new_user.email=email
                new_user.username=email
                new_user.password=setPassword(password)
                new_user.save()
            else:
                error_message='邮箱已经被注册，请登录'
        else:
            error_message='邮箱不能为空'
    return render(request,'register.html',locals())

def login(request):
    error_message=''
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if email:
            user=LoginUser.objects.filter(email=email).first()
            if user:
                db_password= user.password
                password=setPassword(password)
                if db_password==password:
                    response=HttpResponseRedirect('/index/')
                    response.set_cookie('username',user.username)
                    response.set_cookie('user_id',user.id)
                    request.session['username']=user.username
                    return response
                else:
                    error_message='密码错误'
            else:
                error_message='用户名不存在'
        else:
            error_message='邮箱不可以为空'
    return render(request,'login.html',locals())

def index(request):
    return render(request,'index.html')
# Create your views here.
