from django import forms
from blog.models.post import Comment, Post
from ckeditor.widgets import CKEditorWidget
from blog.models.author import Author



class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = [
            'title',
            'overview',
            'thumbnail',
            'categories',
            'content',
            'featured',
            'previous_post',
            'next_post'
        ]


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': "Type your comment",
        'id': 'usercomment',
        'rows': '4'
    }))

    class Meta:
        model = Comment
        fields = ('content',)


# Profile Form
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = [
            'author',
            'image',
            'bio',
            'location',
            'birth_date',
            ]
