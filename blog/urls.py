from django.urls import path

from blog.views import (
    indexView
)

app_name = 'blog'

urlpatterns = [
    path('', indexView, name='index-view'),

]
