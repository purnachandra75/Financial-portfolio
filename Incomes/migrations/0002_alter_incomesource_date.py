# Generated by Django 5.1 on 2024-11-05 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incomes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomesource',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
