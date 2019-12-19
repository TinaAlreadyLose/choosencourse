from django.db import models


# Create your models here.
class Chosenlist(models.Model):
    sid = models.CharField(primary_key=True, max_length=20)
    cid = models.CharField(max_length=20)
    cldate = models.DateField()

    class Meta:
        managed = False
        db_table = 'chosenlist'
        unique_together = (('sid', 'cid'),)


class Course(models.Model):
    cid = models.CharField(primary_key=True, max_length=20)
    cname = models.CharField(max_length=20)
    cmark = models.IntegerField()
    mids = models.CharField(max_length=255)
    tids = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'course'


class Major(models.Model):
    mid = models.CharField(primary_key=True, max_length=20)
    mname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'major'


class Student(models.Model):
    sid = models.CharField(primary_key=True, max_length=20)
    mid = models.CharField(max_length=20)
    sname = models.CharField(max_length=20)
    ssex = models.CharField(max_length=10)
    sbirthdate = models.DateField()
    shiredate = models.DateField()
    degree = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'student'


class Teacher(models.Model):
    tid = models.CharField(primary_key=True, max_length=20)
    tname = models.CharField(max_length=20)
    tsex = models.CharField(max_length=10)
    tbirthdate = models.DateField()
    thiredate = models.DateField()

    class Meta:
        managed = False
        db_table = 'teacher'
