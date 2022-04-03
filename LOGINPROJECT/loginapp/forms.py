from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .import models

class loginform(forms.ModelForm):
    class Meta:
        model=models.logintable
        fields="__all__"