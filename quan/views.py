from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from quan.models import Post


def index(request):
    latest_post_list = Post.objects.order_by('-add_time')[:5]
    output = ', '.join([p.content for p in latest_post_list])
    return HttpResponse(output)


def post(request, post_id):
    _post = get_object_or_404(Post, pk=post_id)
    return render(request, 'quan/post.html', {'post': _post})


def user(request, user_id):
    return HttpResponse("user=" + user_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
