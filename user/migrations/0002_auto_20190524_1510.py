# Generated by Django 2.0.7 on 2019-05-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, default='noob', max_length=10, unique=True, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
