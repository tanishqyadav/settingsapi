
from datetime import datetime
from django.core import validators
from django import forms
from matplotlib import widgets
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        username = forms.CharField(max_length=20, required=False)
        password = forms.CharField(max_length=20, required=False)
        email = forms.CharField(max_length=20, required=False)
        description = forms.CharField(max_length=20, required=False)

        first_name = forms.CharField(max_length=20, required=False)
        last_name = forms.CharField(max_length=20, required=False)

        is_active = forms.BooleanField(required=False)
        
        model = User
        fields = ['username', 'password', 'email', 'description', 'first_name', 'last_name', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True ,attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }