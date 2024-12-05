from django import forms
from X.models import Persona
from X.models import Animales 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class MyLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'


class FormAnimal(forms.ModelForm):
    class Meta:
        model = Animales
        fields = '__all__'
        widgets = {
            'diagnostico': forms.Textarea(attrs={ 
                'class': 'form-group',
                'rows': 10,
                'cols': 50,
                'style': 'width: 50%; height: 150px;',
                
            }),
        
            'datos': forms.Textarea(attrs={
                'class': 'form-group', 
                'rows': 10,
                'cols': 50,
                'style': 'width: 50%; height: 150px;',
            }),
        } 
