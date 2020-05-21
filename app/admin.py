from django.contrib import admin

from .models import App
from .forms import AppModelForm

class AppModelAdmin(admin.ModelAdmin):
    form = AppModelForm

admin.site.register(App, AppModelAdmin)
