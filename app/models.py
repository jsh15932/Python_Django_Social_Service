from django.db import models
from django.conf import settings

from django.views.generic import DetailView, ListView, CreateView
from .forms import AppModelForm

class App(models.Model):
    content = models.CharField(max_length = 140)
    timestamp = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return str(self.content)

class AppCreateView(CreateView):
    form_class = AppModelForm
    template_name = 'app/create_view.html'