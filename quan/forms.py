from django.forms import ModelForm

from quan.models import Article

__author__ = 'youzipi'


class ArticleForm(ModelForm):
    # caption = forms.CharField(label='title',max_length=5)
    # content = forms.CharField(widget=MarkdownWidget())
    # content = forms.CharField(label='content')
    class Meta:
        model = Article
        fields = ['content', 'author']
