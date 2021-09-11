from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string, get_template
from .tokens import account_activation_token
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template import Context


# Create your views here.

class SignUpView(View):
    form_class = RegisterForm
    template_name = 'accounts/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account till it is confirmed
            user.save()

            current_site = get_current_site(request)

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            htmly = get_template('accounts/email.html')
            d = {'username': username, 'domain': current_site.domain,
                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                 'token': account_activation_token.make_token(user)}
            subject, from_email, to = 'Activate Your MySite Account', 'corrupthunt@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, 'Please Confirm your email to complete registration.')

            return redirect('login')

        return render(request, self.template_name, {'form': form})


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.email_confirmed = True
            user.save()
            auth_views.LoginView(request=request, user=request)
            messages.success(request, 'Your account have been confirmed.')
            return redirect('home')
        else:
            messages.warning(request, ('The confirmation link was invalid, '
                                       'possibly because it has already been used.'))
            return redirect('home')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def profileupdate(request):
    if request.method == 'POST':
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        print(pform)

        if pform.is_valid:
            pform.save()
            return redirect('profile')

    else:
        pform = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'accounts/profileupdate.html', {'pform': pform})
