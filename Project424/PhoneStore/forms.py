from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Phone

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(label='Email')
#     first_name = forms.CharField(label='First Name')
#     last_name = forms.CharField(label='Last Name')
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        password1 = forms.CharField(widget=forms.PasswordInput)
        password2= forms.CharField(widget=forms.PasswordInput)
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')


# class Meta:
#     model = User
#     fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')



class ItemForm(forms.ModelForm):
      class Meta:
            model = Phone
            fields = ('name' , 'manufacturer' , 'price' , 'description')
            labels = {
                 'name' : '',
                 'manufacturer' : '',
                 'price' : '',
                 'description' : '',
            }