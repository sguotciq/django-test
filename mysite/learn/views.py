# -*-coding:utf-8-*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from .forms import AddForm
 
def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

def home(request):
	string = u"我在自强学堂学习Django，用它来建网站"
	TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
	info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
	List = ['自强学堂', '渲染Json到模板']
	Dict = {'site': '自强学堂', 'author': '涂伟忠'}
	if request.method == 'POST':# 当提交表单时
		form = AddForm(request.POST) # form 包含提交的数据
		if form.is_valid():# 如果提交的数据合法
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			return HttpResponse(str(int(a)+int(b)))
	else:
		form = AddForm()# 当正常访问时
	return render(request, 'home.html', {'string':string,'TutorialList':TutorialList,'info_dict': info_dict, 'List':json.dumps(List), 'Dict':json.dumps(Dict), 'form':form,})

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request,a,b):
	c = int(a) + int(b)
	return HttpResponse(str(c))
