# -*-coding:utf-8-*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
 
def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

def home(request):
	string = u"我在自强学堂学习Django，用它来建网站"
	TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
	info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
	List = ['自强学堂', '渲染Json到模板']
	Dict = {'site': '自强学堂', 'author': '涂伟忠'}
	return render(request, 'home.html', {'string':string,'TutorialList':TutorialList,'info_dict': info_dict, 'List':json.dumps(List), 'Dict':json.dumps(Dict),})

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request,a,b):
	c = int(a) + int(b)
	return HttpResponse(str(c))
