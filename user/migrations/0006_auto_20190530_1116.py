# Generated by Django 2.0.7 on 2019-05-30 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190529_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(),
        ),
    ]
