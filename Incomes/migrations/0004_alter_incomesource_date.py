# Generated by Django 5.1 on 2024-11-14 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incomes', '0003_registerincome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomesource',
            name='date',
            field=models.DateTimeField(),
        ),
    ]