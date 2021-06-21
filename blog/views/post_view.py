from django.shortcuts import render, get_object_or_404
from blog.models.post import Post
from .category_count_view import get_category_count


def postView(request, id):
    category_count = get_category_count()
    latest_post = Post.objects.order_by('-timestamp')[0:3]
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
        'category_count': category_count,
        'latest_post': latest_post,
    }
    return render(request, 'post.html', context)
