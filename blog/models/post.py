from django.db import models
from .author import Author
from .category import Category
from django.utils.safestring import mark_safe
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    overview = models.TextField(default='not available')
    thumbnail = models.ImageField(upload_to='post', default='no_image.jpeg')
    content = RichTextUploadingField(default='no content available')
    view_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=True)
    previous_post = models.ForeignKey('self', on_delete=models.SET_NULL,
                                      related_name='previous',
                                      blank=True, null=True)
    next_post = models.ForeignKey('self', on_delete=models.SET_NULL,
                                  related_name='next',
                                  blank=True, null=True)

    def __str__(self):
        return str(self.title)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.thumbnail.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def get_absolute_url(self):
        return reverse('post-view', kwargs={
            'id': self.id,
        })

    def get_update_url(self):
        return reverse('post-update', kwargs={
            'id': self.id,
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'id': self.id,
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
