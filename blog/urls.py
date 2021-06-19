from django.urls import path

from blog.views import (
    indexView,
    blogView,
    postView,
)

app_name = 'blog'

urlpatterns = [
    path('', indexView, name='index-view'),
    path('blog/', blogView, name='blog-view'),

]
