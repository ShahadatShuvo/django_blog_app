from django.shortcuts import render
from blog.models.post import Post

def blogView(request):
    blog_list = Post.objects.all()

    context = {
        'blog_list': blog_list,
    }
    return render(request, 'blog.html', context)