# Generated by Django 5.1 on 2024-11-02 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usercradintials', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='confirmPassword',
        ),
    ]
