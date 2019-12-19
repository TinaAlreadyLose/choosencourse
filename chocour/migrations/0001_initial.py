# Generated by Django 2.2.7 on 2019-12-01 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chosenlist',
            fields=[
                ('sid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cid', models.CharField(max_length=20)),
                ('cldate', models.DateField()),
            ],
            options={
                'db_table': 'chosenlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=20)),
                ('cmark', models.IntegerField()),
                ('mids', models.CharField(max_length=255)),
                ('tids', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('mid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('mname', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'major',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('mid', models.CharField(max_length=20)),
                ('sname', models.CharField(max_length=20)),
                ('ssex', models.CharField(max_length=2)),
                ('sbirthdate', models.DateField()),
                ('shiredate', models.DateField()),
                ('degree', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=20)),
                ('tsex', models.CharField(max_length=2)),
                ('tbirthdate', models.DateField()),
                ('thiredate', models.DateField()),
            ],
            options={
                'db_table': 'teacher',
                'managed': False,
            },
        ),
    ]
