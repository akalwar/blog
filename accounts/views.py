from django.shortcuts import render

# signup view

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
