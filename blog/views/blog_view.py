from django.shortcuts import render
from blog.models.post import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blogView(request):
    blog_list = Post.objects.all()
    paginator = Paginator(blog_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    # latest_post = Post.objects.order_by('-timestamp')[0:3]

    context = {
        'blog_list': blog_list,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        # 'most_recent': latest_post,
    }
    return render(request, 'blog.html', context)
