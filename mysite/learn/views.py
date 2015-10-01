# -*-coding:utf-8-*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
 
def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

def home(request):
	string = u"我在自强学堂学习Django，用它来建网站"
	TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
	info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
	return render(request, 'home.html', {'string':string,'TutorialList':TutorialList,'info_dict': info_dict,})

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request,a,b):
	c = int(a) + int(b)
	return HttpResponse(str(c))
