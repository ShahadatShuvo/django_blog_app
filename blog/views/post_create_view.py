from django.shortcuts import render, redirect, reverse
from blog.models.author import Author
from blog.forms import PostForm


def get_author(user):
    qs = Author.objects.filter(author=user)
    if qs.exists():
        return qs[0]
    return None


def post_create(request):
    title = 'create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post-view', kwargs={
                'id': form.instance.id
            }))

    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'post_create.html', context)
