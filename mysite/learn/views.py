# -*-coding:utf-8-*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
 
def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

def home(request):
	return render(request, 'home.html')

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request,a,b):
	c = int(a) + int(b)
	return HttpResponse(str(c))
