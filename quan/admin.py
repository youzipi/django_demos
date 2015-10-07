from django.contrib import admin

from quan.models import Article, User

admin.site.register(User)
admin.site.register(Article)
# admin.site.register(MarkdownModelAdmin)
