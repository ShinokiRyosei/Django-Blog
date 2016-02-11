from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django import forms


class Article(models.Model):
    article = models.TextField()
    post_date = models.DateTimeField('date posted')
    title = models.CharField(max_length=128)


    def _str_(self):
        return self.article


class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
# Create your models here.