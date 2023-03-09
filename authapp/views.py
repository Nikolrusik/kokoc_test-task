from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from authapp import forms

class RegiserView(CreateView):
    model = get_user_model()
    form_class = forms.RegisterForm
    success_url = reverse_lazy("mainapp:main")

class CustomLoginView(LoginView):
    template_name = "authapp/login.html"
