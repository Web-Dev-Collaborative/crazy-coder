from django.shortcuts import render
from posts.models import Post
from django.views import generic


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'