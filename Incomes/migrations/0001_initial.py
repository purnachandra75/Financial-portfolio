# Generated by Django 5.1 on 2024-11-05 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usercradintials', '0003_userdetails_created_at_userdetails_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('source', models.CharField(max_length=40)),
                ('frequency', models.CharField(choices=[('one_time', 'one_time'), ('monthly', 'monthly'), ('Quarterly', 'Quarterly'), ('Halfyealy', 'Halfyealy'), ('Yearly', 'Yearly')], max_length=20)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usercradintials.userdetails')),
            ],
        ),
    ]
