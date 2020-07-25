from django import forms
from .models import Post, CustomUser

# from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        labels = {'username': '아이디', 'password': '비밀번호'}

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password',  'phone_number']
        labels = {'username': '아이디', 'email': '이메일 주소', 'password': '비밀번호', 'phone_number': '휴대폰번호'}
