from django.urls import path

from post.views import (
    indexView,
    blogView,
    postView,
)

app_name = 'post'

urlpatterns = [
    path('', indexView, name='post-index'),
    path('blog/', blogView, name='post-blog'),
    path('post/', postView, name='post-post'),

]
