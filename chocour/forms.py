from django import forms
from . import models


class StuInfo(forms.Form):
    degrees = (
        ('bachelor', '本科'),
        ('associate ', '专科')
    )
    gender = (
        ('male', '男'),
        ('female', '女')
    )

    # def __init__(self):
    #     allMajor = models.Major.objects.all()
    #     LMajor = []
    #     for i in allMajor:
    #         temp = []
    #         temp.append(i.mid)
    #         temp.append(i.mname)
    #         LMajor.append(tuple(temp))
    #     TMajor = tuple(LMajor)
    #     self.major = forms.ChoiceField(label='系别', choices=TMajor)
    name = forms.CharField(label="姓名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='身份', choices=gender)
    birthday = forms.DateField(label='出生日期')
    hireDate = forms.DateField(label='入学日期')
    degree = forms.ChoiceField(label='层次', choices=degrees)


class TeaInfo(forms.Form):
    gender = (
        ('male', '男'),
        ('female', '女')
    )
    tname = forms.CharField(label="教工名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tsex = forms.ChoiceField(label='身份', choices=gender)
    tbirthday = forms.DateField(label='出生日期')
    thireDate = forms.DateField(label='任教日期')


class courInfo(forms.Form):
    marks = (
        (2, '两学分'),
        (4, '四学分'),
        (6, '六学分'),
        (8, '八学分'),
    )
    cid = forms.CharField(label="课程编号", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cname = forms.CharField(label="课程名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cmark = forms.ChoiceField(label='身份', choices=marks)


class majorInfo(forms.Form):
    mid = forms.CharField(label="系id", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mname = forms.CharField(label="系名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
