# Generated by Django 2.1.8 on 2019-05-08 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_mainphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mainphoto',
        ),
    ]
