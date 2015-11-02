from django.contrib import admin

from pieces.models import Card, Record, Tag, User




# admin.site.register(MarkdownModelAdmin)

admin.site.register(User)
admin.site.register(Card)
admin.site.register(Record)
admin.site.register(Tag)
