# -*- coding: utf-8 -*- 
# user: youzipi
# date: 15-10-25 下午11:08

from mongoengine import Document, StringField, connect

connect('test', host='127.0.0.1', port=27017, username='youzipi', password='111')


class PyPost(Document):
    url = StringField()
    pub_time = StringField()
    title = StringField()
    description = StringField()
    a = StringField()

    def __unicode__(self):
        return "%s %s %s %s" % (self.url, self.pub_time, self.title, self.description)


for p in PyPost.objects.all():
    try:
        print p
    except Exception:
        print p.url
