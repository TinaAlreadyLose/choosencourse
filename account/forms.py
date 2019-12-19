from django import forms

from captcha.fields import CaptchaField


class UserForm(forms.Form):
    roles = (
        ('student', '学生'),
        ('teacher', '老师'),
    )
    username = forms.CharField(label="学号/工号", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    captcha = CaptchaField(label='验证码')
    role = forms.ChoiceField(label='身份', choices=roles)


class RegisterForm(forms.Form):
    roles = (
        ('student', '学生'),
        ('teacher', '老师'),
    )
    num = forms.CharField(label="学号/工号", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(label="昵称", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(label='身份', choices=roles)
    captcha = CaptchaField(label='验证码')
