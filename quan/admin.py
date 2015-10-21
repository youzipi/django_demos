from django.contrib import admin

from quan.models import Article, User


# admin.site.register(MarkdownModelAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['content', 'category', 'tags']


admin.site.register(Article, ArticleAdmin)
admin.site.register(User)
