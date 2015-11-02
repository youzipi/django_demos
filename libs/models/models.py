# -*- coding: utf-8 -*- 
# user: youzipi
# date: 15-11-2 下午1:54

from __future__ import division, unicode_literals, print_function
from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.id = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def only_one(cls):
        return cls.objects.get(id=1)
