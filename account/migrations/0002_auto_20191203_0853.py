# Generated by Django 2.2.7 on 2019-12-03 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuId', models.CharField(max_length=128, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('student', '学生'), ('teacher', '教师')], default='学生', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-c_time'],
            },
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]