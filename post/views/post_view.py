from django.shortcuts import render


def postView(request):
    return render(request, 'post.html', context={})