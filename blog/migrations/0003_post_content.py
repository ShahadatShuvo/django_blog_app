# Generated by Django 3.2.4 on 2021-06-21 15:32

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
    ]
