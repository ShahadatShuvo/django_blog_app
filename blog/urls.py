from django.urls import path

from blog.views import (
    index,
    blog,
    post,
)

app_name = 'blog'

urlpatterns = [
    path('', index, name='index-view'),
    path('blog/', blog, name='blog-view'),
    path('post/', post, name='post-view'),

]
