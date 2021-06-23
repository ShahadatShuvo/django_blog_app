from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import (
    postView,
    post_create,
    post_update,
    post_delete
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),

    path('', include('blog.urls')),
    path('create/', post_create, name='post-create'),
    path('post/<id>/', postView, name='post-view'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
