from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

#this is for user profile update form
class UserUpdateForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class PasswordUpdateForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    


    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
