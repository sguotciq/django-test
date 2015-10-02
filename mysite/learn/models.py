# -*- coding:utf-8 -*-
from django.db import models
from .fields import *


# Create your models here.
class Person(models.Model):
	name = models.CharField(u'name',max_length=30)
	age = models.IntegerField(u'age')
	def __unicode__(self):# 在Python3中使用 def __str__(self):
		return self.name

class Article(models.Model):
	labels = ListField('labels')
	title = models.CharField('title',max_length=100)
	content = models.CharField('content',max_length=3000)
	def __unicode__(self):# 在Python3中使用 def __str__(self):
		return self.title


class Blog(models.Model):
    name = models.CharField('name',max_length=100)
    tagline = models.TextField('tagline')
 
    def __unicode__(self):  # __str__ on Python 3
        return self.name
 
class Author(models.Model):
    name = models.CharField('name',max_length=50)
    email = models.EmailField()
 
    def __unicode__(self):  # __str__ on Python 3
        return self.name
 
class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()
 
    def __unicode__(self):  # __str__ on Python 3
        return self.headline