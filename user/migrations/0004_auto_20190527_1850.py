# Generated by Django 2.0.7 on 2019-05-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190524_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=5)),
            ],
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='profile',
        ),
    ]
