# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import json

# Create your views here.

def home(request):
	string = u"我在自强学堂学习Django，用它来建网站"
	return render(request, 'home.html', {'string': string})

def home2(request):
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    # return render(request, 'home2.html', {'TutorialList': TutorialList})
    return render(request, 'home2.html', {'info_dict': info_dict})


 
def home3(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
    return render(request, 'home3.html', {'List': json.dumps(List),
    				'Dict': json.dumps(Dict)})
