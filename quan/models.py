# coding=utf-8
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class User(models.Model):
    name = models.CharField("user name", max_length=20)
    email = models.EmailField()
    register_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Article(models.Model):
    content = models.CharField(max_length=200)
    add_time = models.DateTimeField()
    category = models.CharField(max_length=20,default="uncategory")
    tags = models.CharField(max_length=200, default="no-tag", verbose_name=u'标签', help_text=u'用逗号分隔')
    author = models.ForeignKey(User)

    def get_tags(self):
        return self.tags.split(',')

    def __str__(self):
        return self.content.encode('utf-8') # 中文问题

