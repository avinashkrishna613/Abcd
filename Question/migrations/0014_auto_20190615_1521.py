# Generated by Django 2.0.7 on 2019-06-15 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0013_auto_20190603_2215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ques',
            options={'ordering': ['pk']},
        ),
    ]
