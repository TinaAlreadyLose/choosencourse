from django.shortcuts import render

from django.shortcuts import redirect, reverse
from . import models
from . import forms
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def index(request):
    return render(request, 'account/index.html')


# 注册
def register(request):
    if request.session.get('is_login', None):
        return redirect(reverse('account:login'))

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            num = register_form.cleaned_data.get('num')
            nickname = register_form.cleaned_data.get('nickname')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            role = register_form.cleaned_data.get('role')
            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'account/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(num=num)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'account/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'account/register.html', locals())

                new_user = models.User()
                new_user.num = num
                new_user.name = nickname
                new_user.password = make_password(password1, None, 'pbkdf2_sha256')
                new_user.email = email
                new_user.role = role
                new_user.save()
                return redirect(reverse('account:login'))
        else:
            return render(request, 'account/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'account/register.html', locals())


# 登入
def login(request):
    if request.session.get('is_login', None):  # 不允许重复登入
        return redirect(reverse('account:login'))
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # print(username, password)
        message = '请检查填写内容'
        # if username.strip() and password:
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            role = login_form.cleaned_data.get('role')
            try:
                user = models.User.objects.get(num=username, role=role)
            except:
                message = '用户不存在'
                return render(request, 'account/login.html', locals())
            if check_password(password, user.password):  # 登入成功
                request.session['is_login'] = True
                request.session['user_num'] = user.num
                request.session['user_role'] = role
                # print(user.password)
                # print(role)
                print(request.session['user_num'])
                return redirect(reverse('account:index'))
            else:
                message = '密码错误'
                return render(request, 'account/login.html', locals())
        else:
            return render(request, 'account/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'account/login.html', locals())


# 登出
def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect(reverse('account:login'))
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect(reverse('account:login'))
