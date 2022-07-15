from django import forms
from . models import Dishes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation


class AddNewProduct(forms.ModelForm):
    class Meta:
        model = Dishes
        fields = '__all__'

class UserCreate(UserCreationForm):
    password1 = forms.CharField(label=('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter Password'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm Password'}),
                                help_text=('Just Enter the same password, for confirmation'))
    class Meta:
        model = User
        fields= ('username', 'password1', 'password2',)

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}),
        }