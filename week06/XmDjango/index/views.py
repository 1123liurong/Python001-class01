from django.shortcuts import render,redirect
from .models import Shorts
# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello Django!")

# def year(request,year):
#     # return HttpResponse(year)
#     return redirect('/2020.html') #redirect 一般应用登录页面跳转

# def name(request,**kwargs):
#     return HttpResponse(kwargs['name']) #kwargs 取关键参数year/name 

# def myyear(request,year):
#     return render(request,'yearview.html') # rend 和模板绑定

def short(request):
    s = Shorts.objects.all
    return render(request,'index.html',locals())#locals() 获取所有本地变量传给模板，使用render自动寻转templates目录下的文件
