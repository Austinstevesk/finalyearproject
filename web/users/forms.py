from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control', 'required':'required'}),
        'last_name':forms.TextInput(attrs={'class':'form-control', 'required':'required'}),
        'email':forms.EmailInput(attrs={'class':'form-control', 'required':'required'}),
        #'phone':forms.TextInput(attrs={'class':'form-control', 'required':'required'}),
        'password1':forms.PasswordInput(attrs={'class':'form-control'}),
        'password2':forms.PasswordInput(attrs={'class':'form-control'}),
    }



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
