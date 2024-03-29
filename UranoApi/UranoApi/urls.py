"""UranoApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as acc_views
from accounts.forms import CustomLoginForm, MailsPasswordResetForm, ResetPasswordForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feed.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=CustomLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', acc_views.SignUpView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', acc_views.ActivateAccount.as_view(), name='activate'),
    path('profile/', acc_views.profile, name='profile'),
    path('profile/<str:username>/', acc_views.profile, name='profile'),
    path('profileupdate/', acc_views.profileupdate, name='profileupdate'),
    path('redirect/', acc_views.Redirect.as_view(template_name='accounts/redirect.html'), name='redirect'),
    path('', include('social_django.urls', namespace='social')),
    path('settings/', acc_views.settings, name='settings'),
    path('settings/password/', acc_views.password, name='password'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/mail_password.html', form_class=MailsPasswordResetForm), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html' ,form_class=ResetPasswordForm), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done'), name= "password_reset_complete"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

