from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User,  Create_Test_ClassRoom# Use default User if not customizing

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    pass


class CustomTestClassroom(forms.ModelForm):
    class Meta:
        model = Create_Test_ClassRoom
        fields = ['Name_Test', 'Discription','App_Name' ,'Start_Time', 'End_Time']
        widgets = {
            'Name_Test': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter test name'
            }),
            'Discription': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter test description', 
                'rows': 3
            }),
            'App_Name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter whitelisted app name(s) e.g., VSCode, Chrome'
            }),
            'Start_Time': forms.DateTimeInput(attrs={
                'type': 'datetime-local', 
                'class': 'form-control'
            }),
            'End_Time': forms.DateTimeInput(attrs={
                'type': 'datetime-local', 
                'class': 'form-control'
            }),
        }

from django import forms
from .models import Create_Test_ClassRoom


class CustomAccessForm(forms.Form):
    Access_Token = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter access token'
        })
    )

