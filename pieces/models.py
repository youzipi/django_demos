# coding=utf-8

from django.db import models
from django.utils import timezone

from libs.models.mixins import QueryMixin


class TimeMixin(models.Model):
    class Meta:
        abstract = True
        ordering = ['-add_time']

    add_time = models.DateTimeField(u"添加时间", default=timezone.now)
    update_time = models.DateTimeField(u"修改时间", default=timezone.now)


class User(TimeMixin):
    name = models.CharField("user name", max_length=20, unique=True)
    email = models.EmailField(unique=True, error_messages={'unique': "this email address is registered"})
    register_date = models.DateTimeField()

    def __str__(self):
        return self.name.encode('utf-8')


class Tag(TimeMixin, QueryMixin):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name.encode('utf-8')


class Card(TimeMixin, QueryMixin):
    class Meta:
        ordering = ['id', 'add_time']

    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    category = models.CharField(max_length=20, default="uncategory")
    tags = models.ManyToManyField(Tag)
    add_user = models.ForeignKey(User)

    def get_tags(self):
        return self.tags

    @property
    def record_count(self):
        return self.record_set.count()

    # def records(self):
    #     return self.record_set

    def __str__(self):
        return self.name.encode('utf-8')  # 中文问题


class Record(TimeMixin):
    card = models.ForeignKey(Card)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content[:20].encode('utf-8')  # 中文问题
