# Generated by Django 2.2.7 on 2019-12-03 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191203_0853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='stuId',
            new_name='num',
        ),
    ]