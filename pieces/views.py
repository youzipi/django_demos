# coding=utf-8
import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView

from libs.decorator import log0
from pieces.models import Card, Record
from quan.forms import ArticleForm



# 缓存
# try:
#    cache = caches['memcache']
# except ImportError as e:
#    cache = caches['default']

# logger
from quan.mongo_models import PyPost

logger = logging.getLogger(__name__)


class HomePageView(TemplateView):
    template_name = 'pieces/index.html'
    model = Card

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        cards = Card.objects.all()

        for card in cards:
            rel_records = Record.objects.filter(card=card).count()
            setattr(card, 'records', rel_records)
        context['cards'] = cards
        return context


class DashBroadView(ListView):
    template_name = 'pieces/dashbroad.html'
    context_object_name = 'cards'
    model = Card


class CardView(TemplateView):
    template_name = 'pieces/card.html'
    model = Card

    @log0
    def get_context_data(self, **kwargs):
        context = super(CardView, self).get_context_data(**kwargs)
        card = Card.objects.get(**kwargs)
        context['card'] = card
        return context


class TagView(View):
    def get(self, request):
        tags = request.GET
        print tags


def new(request):
    return render(request, 'quan/edit.html', {'form': ArticleForm})


def user(request, user_id):
    return HttpResponse("user=" + user_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


class AboutView(TemplateView):
    template_name = "quan/about.html"


class PyPostView(ListView):
    template_name = "quan/py_post.html"
    context_object_name = 'py_post_list'
    model = PyPost
    queryset = PyPost.objects.all()
