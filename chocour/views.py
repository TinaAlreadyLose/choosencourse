from django.shortcuts import render

from django.shortcuts import redirect, reverse

from . import models
from . import forms
import datetime


# Create your views here.
def prefectInformation(request):
    # if not request.session.get('is_login', None):
    print(request.session['user_role'])
    if request.session['user_role'] == 'student':
        if request.method == 'POST':
            # print('post')
            stuInfo_form = forms.StuInfo(request.POST)
            major = request.POST.get('major')
            if stuInfo_form.is_valid():
                # print('get data')
                num = request.session['user_num']
                # major = stuInfo_form.cleaned_data.get('major')
                name = stuInfo_form.cleaned_data.get('name')
                sex = stuInfo_form.cleaned_data.get('sex')
                birthday = stuInfo_form.cleaned_data.get('birthday')
                hireDate = stuInfo_form.cleaned_data.get('hireDate')
                degree = stuInfo_form.cleaned_data.get('degree')
                try:
                    # print('add data')
                    new_student = models.Student()
                    new_student.sid = num
                    new_student.mid = major
                    new_student.sname = name
                    new_student.ssex = sex
                    new_student.sbirthdate = birthday
                    new_student.shiredate = hireDate
                    new_student.degree = degree
                    new_student.save()
                except:
                    return redirect(reverse('account:index'))
                return redirect(reverse('account:index'))
        stuInfo_form = forms.StuInfo()
        Major = models.Major.objects.all()
        return render(request, 'chocour/stuPrefectInformation.html', locals())
    elif request.session['user_role'] == 'teacher':
        if request.method == 'POST':
            teaInfo_form = forms.TeaInfo(request.POST)
            if teaInfo_form.is_valid():
                tid = request.session['user_num']
                tname = teaInfo_form.cleaned_data.get('tname')
                tsex = teaInfo_form.cleaned_data.get('tsex')
                tbirthday = teaInfo_form.cleaned_data.get('tbirthday')
                thireDate = teaInfo_form.cleaned_data.get('thireDate')
                try:
                    new_teacher = models.Teacher()
                    new_teacher.tid = tid
                    new_teacher.tname = tname
                    new_teacher.tsex = tsex
                    new_teacher.tbirthdate = tbirthday
                    new_teacher.thiredate = thireDate
                    new_teacher.save()
                except:
                    return redirect(reverse('account:index'))
            return redirect(reverse('account:index'))

        teaInfo_form = forms.TeaInfo()
        return render(request, 'chocour/teaPrefectInfomation.html', locals())

    return redirect(reverse('account:login'))


# 添加刀数据库的列表可以用eval转化成list,用str转换成str
def setCourse(request):
    if request.method == 'POST' and request.session['user_role'] == 'teacher':
        course_form = forms.courInfo(request.POST)
        majorids = request.POST.getlist('mids')
        teacherids = request.POST.getlist('tids')
        print('post')
        if course_form.is_valid():
            cid = course_form.cleaned_data.get('cid')
            cname = course_form.cleaned_data.get('cname')
            cmark = course_form.cleaned_data.get('cmark')
            try:
                new_course = models.Course()
                new_course.cid = cid
                new_course.cname = cname
                new_course.cmark = int(cmark)
                new_course.tids = str(teacherids)
                new_course.mids = str(majorids)
                new_course.save()
            except:
                return redirect(reverse('account:index'))

            return redirect(reverse('account:index'))

    majors = models.Major.objects.all()
    teachers = models.Teacher.objects.all()
    course_form = forms.courInfo()
    print('not post')
    return render(request, 'chocour/course.html', locals())


def addMajor(request):
    if request.method == 'POST' and request.session['user_role'] == 'teacher':
        major_form = forms.majorInfo(request.POST)
        if major_form.is_valid():
            mid = major_form.cleaned_data.get('mid')
            mname = major_form.cleaned_data.get('mname')
            print(mname)
            try:
                new_major = models.Major()
                new_major.mid = mid
                new_major.mname = mname
                new_major.save()
            except:
                return redirect(reverse('account:index'))

        return redirect(reverse('account:index'))
    major_form = forms.majorInfo()
    return render(request, 'chocour/major.html', locals())


def chorcour(request):
    if request.method == 'POST' and request.session['user_role'] == 'student':
        coursename = request.POST['cour']
        print(coursename)
        course1 = models.Course.objects.get(cname=coursename)
        new_chosenlist = models.Chosenlist()
        new_chosenlist.sid = request.session['user_num']
        new_chosenlist.cid = course1.cid
        new_chosenlist.cldate =datetime.date.today()
        new_chosenlist.save()
        return redirect(reverse('account:index'))
    if request.session['user_role'] == 'student':
        student = models.Student.objects.get(sid=request.session['user_num'])
        # print(student.mid)
        course = models.Course.objects.all()
        # Coursesid = []
        Coursesname = []
        for c in course:
            cour = []
            if student.mid in eval(c.mids):
                # print(eval((c.mids)))
                # Coursesid.append(c.cid)
                Coursesname.append(c.cname)
        # Courses = zip(Coursesid, Coursesname)
        # for key, value in Courses:
        #     print(key, value)
        return render(request, 'chocour/chorour.html', locals())

    return render(request, 'chocour/chorour.html', locals())
