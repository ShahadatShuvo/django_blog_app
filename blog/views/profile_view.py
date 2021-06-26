from django.urls import reverse_lazy
from django.views.generic import UpdateView
from blog.forms import ProfileForm
from blog.models.author import Author


# Edit Profile View
class ProfileView(UpdateView):
    model = Author
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/profile.html'
