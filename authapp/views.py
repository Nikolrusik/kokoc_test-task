from typing import Dict, Any
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from authapp import forms, models
from mainapp import models as mainapp_models


class RegiserView(CreateView):
    model: Any = get_user_model()
    form_class: Any = forms.RegisterForm
    success_url: str = reverse_lazy("mainapp:main")


class CustomLoginView(LoginView):
    template_name: str = "authapp/login.html"


class ProfileView(TemplateView):
    template_name: str  = "authapp/profile.html"

    def get_context_data(self, pk: int = None, **kwargs: Any) -> Dict[str, Any]:
        context = super(ProfileView, self).get_context_data(**kwargs)
        context["viewed_user"] = models.AbstractUserModel.objects.get(id=pk)
        context["surveys"] = mainapp_models.CompletedSurveyModel.objects.filter(
            user__id=pk)
        return context


class UsersView(TemplateView):
    template_name: str = "authapp/user_list.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(UsersView, self).get_context_data(**kwargs)
        context['all_users'] = models.AbstractUserModel.objects.all()
        return context
