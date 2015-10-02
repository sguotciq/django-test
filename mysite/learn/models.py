# -*- coding:utf-8 -*-
from django.db import models
from .fields import *


# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	def __unicode__(self):# 在Python3中使用 def __str__(self):
		return self.name

class Article(models.Model):
	labels = ListField()
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=3000)
	def __unicode__(self):# 在Python3中使用 def __str__(self):
		return self.title
