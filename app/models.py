from django.db import models
from django.conf import settings

from django.views.generic import DetailView, ListView, CreateView
from .forms import AppModelForm

class AppCreateView(CreateView):
    form_class = AppModelForm
    template_name = 'app/create_view.html'