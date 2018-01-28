from django.shortcuts import render, HttpResponse
#导入HttpResponse模块
# Create your views here.

def login(request):
    return HttpResponse('<h1>欢迎来到Django全明星</h1>')

