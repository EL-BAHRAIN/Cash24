from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib.auth import (
    authenticate, login, logout,
)
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from accounts.forms import (
    RegistrationForm,
    LoginForm,
    EditProfileForm,
)
# Create your views here.

class LandingPageView(TemplateView):
    template_name = "accounts/landing_page.html"



class LoginView(generic.FormView):
    form_class = LoginForm
    # success_url = LOGIN_REDIRECT_URL
    success_url = reverse_lazy('bank:home')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/register.html', args)


def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


#
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect('/accounts/profile')
#         else:
#             return redirect('/accounts/change-password')
#     else:
#         form = PasswordChangeForm(user=request.user)
#         args = {'form': form}
#         return render(request, 'accounts/password_change.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('/accounts/profile'))
    else:
        form = PasswordChangeForm(user=request.user)
    args = {'form': form}
    return render(request, 'accounts/password_change.html', args)




