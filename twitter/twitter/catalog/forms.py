from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from django.contrib.admin.widgets import AdminDateWidget





class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form__input', 'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form__input', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form__input', 'placeholder': 'Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form__input', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form__input', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form__input', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

class DateInput(forms.DateInput):
    input_type = 'date'

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Фамилия'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'ava__profile', 'placeholder': 'Аватар'}), required=False)
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'О себе'}), required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Email', 'readonly': True}))
    date_of_birth = forms.DateField(widget=DateInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'text', 'email', 'date_of_birth')



class UserPostForm(UserChangeForm):
    twitext = forms.CharField(widget=forms.TextInput(attrs={'class': 'text__input'}), required=False)
    img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'ava__profile'}), required=False)

    class Meta:
        model = Post
        fields = ('twitext', 'img')


class CommentForm(forms.ModelForm):
    #post = forms.CharField(widget=forms.TextInput(attrs={'class': 'text__input'}), required=False)
    body = forms.CharField(widget=forms.TextInput(attrs={'class': 'text__input'}), required=False)
    class Meta:
        model = Comment
        fields = ('body',)
