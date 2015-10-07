import datetime

from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import TemplateView, View

from quan.forms import ArticleForm
from quan.models import Article


def index(request):
    latest_post_list = Article.objects.order_by('-add_time')[:5]
    # _posts = ', '.join([p.content for p in latest_post_list])
    _posts = ', '.join([p.content for p in latest_post_list])
    return render(request, 'quan/index.html', {'posts': latest_post_list})


# def post(request, post_id):
#     _post = get_object_or_404(Article, pk=post_id)
#     return render(request, 'quan/post.html', {'post': _post})

class ArticleView(View):
    def get(self, request, post_id):
        _post = get_object_or_404(Article, pk=post_id)
        return render(request, 'quan/post.html', {'article': _post})


class ArticlesView(View):
    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            print(form)
            new_article = form.save(commit=False)
            new_article.add_time = datetime.datetime.now()
            new_article.save()
            form.save_m2m()
            return HttpResponseRedirect('/quan')
        else:
            return render_to_response('quan/edit.html', {'form': form}, context_instance=RequestContext(request))


def new(request):
    return render(request, 'quan/edit.html', {'form': ArticleForm})


def user(request, user_id):
    return HttpResponse("user=" + user_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


class AboutView(TemplateView):
    template_name = "quan/about.html"
