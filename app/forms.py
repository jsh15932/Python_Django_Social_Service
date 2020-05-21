from django import forms

from .models import App

class AppModelForm(forms.ModelForm):
    class Meta:
        model = App
        fields = [
            "content"
        ]