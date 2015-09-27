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


class Post(models.Model):
    content = models.CharField(max_length=1000)
    add_time = models.DateTimeField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.content
