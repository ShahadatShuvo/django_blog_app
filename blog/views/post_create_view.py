from django.shortcuts import render, redirect, reverse

from blog.forms import PostForm, CommentForm


def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'form': form,
    }
    return render(request, 'post_create.html', context)
