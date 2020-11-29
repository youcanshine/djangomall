"""djangomall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns
from django.template.response import TemplateResponse
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import views, forms as auth_forms


def validate_username(name):
    if len(name) > 10:
        raise ValidationError('Username too long')


class NewAuthenticationForm(auth_forms.AuthenticationForm):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
        validators=[validate_username]
    )
    password = forms.CharField(
        label='PASSWORD',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class NewLoginView(views.LoginView):
    template_name = 'accounts/login.html'
    form_class = NewAuthenticationForm


urlpatterns = i18n_patterns(path('admin/', admin.site.urls), prefix_default_language=False)
urlpatterns += [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # re_path(r'^(.*)$', lambda r, s: TemplateResponse(r, 'base.html'))
]
