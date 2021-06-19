from django.shortcuts import render


def postView(request, id):
    return render(request, 'post.html', context={})