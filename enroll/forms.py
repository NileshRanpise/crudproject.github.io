from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id','Name','Email','Password']
        widgets = {
            'Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Email' : forms.EmailInput(attrs={'class':'form-control'}),
            'Password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }