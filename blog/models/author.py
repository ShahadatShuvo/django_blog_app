from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post', default='no_pic.jpg', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.author)

    @receiver(post_save, sender=User)
    def create_author_profile(sender, instance, created, **kwargs):
        if created:
            Author.objects.create(author=instance)

    @receiver(post_save, sender=User)
    def save_author_profile(sender, instance, **kwargs):
        instance.author.save()

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
