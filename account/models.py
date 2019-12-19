from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(models.Model):
    gender = (
        ('student', "学生"),
        ('teacher', "教师"),
    )

    num = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=32, choices=gender, default="学生")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
