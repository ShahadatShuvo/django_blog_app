from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from blog.views import (
    indexView,
    blogView,
    postView,
    post_create,
    post_update,
    post_delete,
    ProfileView,
)
from accounts.views import (
    SignUpView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),

    path('', indexView, name='home-view'),
    path('blog/', blogView, name='blog-view'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/', postView, name='post-view'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),

    # User Signup, Login, Logout, Password Reset
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'
    ), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(
        next_page='home-view'
    ), name='logout'),
    path(
        'accounts/change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/change-password.html',
            success_url='login'
        ),
        name='change_password'
    ),

    # # Forget Password
    # path('accounts/password-reset/',
    #      auth_views.PasswordResetView.as_view(
    #          template_name='accounts/password-reset/password_reset.html',
    #          # subject_template_name='commons/password-reset/password_reset_subject.txt',
    #          email_template_name='accounts/password-reset/password_reset_email.html',
    #          success_url='done/'
    #      ),
    #      name='password_reset'),
    # path('accounts/password-reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(
    #          template_name='accounts/password-reset/password_reset_done.html'
    #      ),
    #      name='password_reset_done'),
    # path('accounts/password-reset-confirm/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(
    #          template_name='accounts/password-reset/password_reset_confirm.html'
    #      ),
    #      name='password_reset_confirm'),
    # path('accounts/password-reset-complete/',
    #      auth_views.PasswordResetCompleteView.as_view(
    #          template_name='accounts/password-reset/password_reset_complete.html'
    #      ),
    #      name='password_reset_complete'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
