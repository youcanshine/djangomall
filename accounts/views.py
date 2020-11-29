from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from accounts.forms import LoginForm, SignupForm
from django.conf import settings
from django.contrib import auth
# Create your views here.


def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)
        redirect_url = 'login'
        if user:
            auth.login(request, user)
            redirect_url = settings.LOGIN_REDIRECT_URL
        return redirect(redirect_url)
    ctx = {'form': form}
    return TemplateResponse(request, 'accounts/signup.html', ctx)


class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm


